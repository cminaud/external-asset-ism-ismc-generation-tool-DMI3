import xml.etree.ElementTree as ET

from external_asset_ism_ismc_generation_tool.common.base_model import BaseModel
from tests.test_utils.ism_manifest_extractor.models.body import Body
from tests.test_utils.ism_manifest_extractor.models.head import Head


class Smil(BaseModel):
    namespace = {'smil': 'http://www.w3.org/2001/SMIL20/Language'}

    xmlns: str
    head: Head
    body: Body

    def __init__(self, xmlns: str, head: Head, body: Body):
        self.xmlns = xmlns
        self.head = head
        self.body = body

    @classmethod
    def from_xml(cls, xml_string: str):
        smil_root = ET.fromstring(xml_string)

        head = Head.from_xml(smil_root.find('smil:head', cls.namespace), Smil.namespace)
        body = Body.from_xml(smil_root.find('smil:body', cls.namespace), Smil.namespace)

        return cls(Smil.namespace.get('smil'), head, body)
