import xml.etree.ElementTree as ET

from external_asset_ism_ismc_generation_tool.common import BaseModel


class Meta(BaseModel):
    name: str
    content: str

    def __init__(self, name: str, content: str):
        self.name = name
        self.content = content

    @classmethod
    def from_xml(cls, meta_element: ET.Element):
        attributes = meta_element.attrib
        name = attributes.get('name')
        content = attributes.get('content')

        return cls(name, content)
