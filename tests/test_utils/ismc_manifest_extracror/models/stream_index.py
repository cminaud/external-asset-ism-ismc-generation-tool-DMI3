import xml.etree.ElementTree as ET
from typing import Optional

from external_asset_ism_ismc_generation_tool.common.base_model import BaseModel
from tests.test_utils.ismc_manifest_extracror.models.chunk_data import ChunkData
from tests.test_utils.ismc_manifest_extracror.models.quality_level import QualityLevel
from tests.test_utils.ismc_manifest_extracror.models.stream_type import StreamType


class StreamIndex(BaseModel):
    stream_type: StreamType
    chunks: str
    quality_levels: str
    url: str
    name: Optional[str]
    language: Optional[str]
    max_width: Optional[str]
    max_height: Optional[str]
    display_width: Optional[str]
    display_height: Optional[str]
    quality_level_list: Optional[list]
    chunk_datas: Optional[list]

    def __init__(self, stream_type: StreamType,
                 chunks: str,
                 quality_levels: str,
                 url: str,
                 name: Optional[str] = None,
                 language: Optional[str] = None,
                 max_width: Optional[str] = None,
                 max_height: Optional[str] = None,
                 display_width: Optional[str] = None,
                 display_height: Optional[str] = None,
                 quality_level_list: Optional[list] = None,
                 chunk_datas: Optional[list] = None):
        self.stream_type = stream_type
        self.chunks = chunks
        self.quality_levels = quality_levels
        self.name = name
        self.language = language
        self.max_width = max_width
        self.max_height = max_height
        self.display_width = display_width
        self.display_height = display_height
        self.url = url
        self.quality_level_list = quality_level_list
        self.chunk_datas = chunk_datas

    @classmethod
    def from_xml(cls, stream_index_element: ET.Element):
        attributes = stream_index_element.attrib
        stream_type = attributes.get('Type')
        chunks = attributes.get('Chunks')
        quality_levels = attributes.get('QualityLevels')
        name = attributes.get('Name')
        language = attributes.get('Language')
        max_width = attributes.get('MaxWidth')
        max_height = attributes.get('MaxHeight')
        display_width = attributes.get('DisplayWidth')
        display_height = attributes.get('DisplayHeight')
        url = attributes.get('Url')
        quality_level_elements = stream_index_element.findall('QualityLevel')
        quality_level_list = [QualityLevel.from_xml(quality_level_element) for quality_level_element in quality_level_elements]
        chunk_data_elements = stream_index_element.findall('c')
        chunk_datas = [ChunkData.from_xml(chunk_data_element) for chunk_data_element in chunk_data_elements]
        return cls(stream_type,
                   chunks,
                   quality_levels,
                   url,
                   name,
                   language,
                   max_width,
                   max_height,
                   display_width,
                   display_height,
                   quality_level_list,
                   chunk_datas)
