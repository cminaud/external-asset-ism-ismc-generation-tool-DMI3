import xml.etree.ElementTree as ET
from typing import Optional

from external_asset_ism_ismc_generation_tool.common.base_model import BaseModel
from tests.test_utils.ism_manifest_extractor.models.param import Param


class TextStream(BaseModel):
    src: str
    system_bitrate: Optional[str]
    system_language: Optional[str]
    params: list

    def __init__(self, src: str, system_bitrate: Optional[str] = None, system_language: Optional[str] = None, params: Optional[list] = None):
        self.src = src
        self.system_bitrate = system_bitrate
        self.system_language = system_language
        self.params = params or []

    def to_xml(self) -> ET.Element:
        textstream_element = ET.Element("textstream")
        textstream_element.set("src", self.src)
        if self.system_bitrate:
            textstream_element.set("systemBitrate", str(self.system_bitrate))
        if self.system_language:
            textstream_element.set("systemLanguage", self.system_language)
        for param_data in self.params:
            param_element = ET.Element("param")
            param_element.set("name", param_data["name"])
            param_element.set("value", param_data["value"])
            param_element.set("valuetype", param_data["valuetype"])
            textstream_element.append(param_element)

        return textstream_element

    @classmethod
    def from_xml(cls, text_stream_element: ET.Element, namespace: dict):
        attributes = text_stream_element.attrib
        src = attributes.get('src')
        system_bitrate = attributes.get('systemBitrate')
        system_language = attributes.get('systemLanguage')
        params = text_stream_element.findall(f'{list(namespace.keys())[0]}:param', namespace)
        param_list = []
        for param in params:
            param_attributes = param.attrib
            param_name = param_attributes.get('name')
            param_value = param_attributes.get('value')
            param_value_type = param_attributes.get('valuetype')
            param_list.append(Param(name=param_name, value=param_value, value_type=param_value_type))
        return cls(src, system_bitrate, system_language, param_list)
