import decimal
import xml.etree.ElementTree as ET
from typing import Optional

from external_asset_ism_ismc_generation_tool.common.base_model import BaseModel


class ChunkData(BaseModel):
    time_start: Optional[str]
    number: Optional[str]
    duration: Optional[decimal.Decimal]
    r: Optional[str]

    def __init__(self, time_start: Optional[str] = None, number: Optional[str] = None, duration: Optional[decimal.Decimal] = None, r: Optional[str] = None):
        self.time_start = time_start
        self.number = number
        self.duration = duration
        self.r = r

    @classmethod
    def from_xml(cls, c_element: ET.Element):
        attributes = c_element.attrib
        time_start = attributes.get('t')
        number = attributes.get('n')
        duration = attributes.get('d')
        r = attributes.get('r')

        return cls(time_start, number, duration, r)
