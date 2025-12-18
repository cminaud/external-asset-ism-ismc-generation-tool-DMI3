import xml.etree.ElementTree as ET
from typing import Optional

from external_asset_ism_ismc_generation_tool.common.base_model import BaseModel
from tests.test_utils.ism_manifest_extractor.models.param import Param


class Video(BaseModel):
    src: str
    system_bitrate: str
    params: list

    def __init__(self, src: str, system_bitrate: str, params: Optional[list] = None):
        self.src = src
        self.system_bitrate = system_bitrate
        self.params = params or []

    @classmethod
    def from_xml(cls, video_element: ET.Element, namespace: dict):
        attributes = video_element.attrib
        src = attributes.get('src')
        system_bitrate = attributes.get('systemBitrate')
        params = video_element.findall(f'{list(namespace.keys())[0]}:param', namespace)
        param_list = []
        for param in params:
            param_attributes = param.attrib
            param_name = param_attributes.get('name')
            param_value = param_attributes.get('value')
            param_value_type = param_attributes.get('valuetype')
            param_list.append(Param(name=param_name, value=param_value, value_type=param_value_type))
        return cls(src, system_bitrate, param_list)
