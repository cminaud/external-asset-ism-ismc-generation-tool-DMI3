import xml.etree.ElementTree as ET
from typing import Optional

from external_asset_ism_ismc_generation_tool.common import BaseModel
from tests.test_utils.ism_manifest_extractor.models.meta import Meta


class Head(BaseModel):
    meta_list: Optional[list]

    def __init__(self, meta_list: Optional[list] = None):
        self.meta_list = meta_list

    @classmethod
    def from_xml(cls, head_element: ET.Element, namespace: dict):
        meta_data_elements = head_element.findall(f'{list(namespace.keys())[0]}:meta', namespace)
        meta_list = [Meta.from_xml(meta_data_element) for meta_data_element in meta_data_elements]

        return cls(meta_list)
