import xml.etree.ElementTree as ET
from typing import Optional

from external_asset_ism_ismc_generation_tool.common.base_model import BaseModel
from tests.test_utils.ismc_manifest_extracror.models.stream_index import StreamIndex


class SmoothStreamingMedia(BaseModel):
    major_version: str
    minor_version: str
    duration: str
    time_scale: Optional[str]
    is_live: Optional[str]
    lookahead_count: Optional[str]
    dvr_window_length: Optional[str]
    stream_indexes: Optional[list]

    def __init__(self, major_version: str,
                 minor_version: str,
                 duration: str,
                 time_scale: Optional[str] = None,
                 is_live: Optional[str] = None,
                 lookahead_count: Optional[str] = None,
                 dvr_window_length: Optional[str] = None,
                 stream_indexes: Optional[list] = None):
        self.major_version = major_version
        self.minor_version = minor_version
        self.duration = duration
        self.time_scale = time_scale
        self.is_live = is_live
        self.lookahead_count = lookahead_count
        self.dvr_window_length = dvr_window_length
        self.stream_indexes = stream_indexes

    @classmethod
    def from_xml(cls, xml_string: str):
        smooth_streaming_media_root = ET.fromstring(xml_string)
        attributes = smooth_streaming_media_root.attrib
        major_version = attributes.get('MajorVersion')
        minor_version = attributes.get('MinorVersion')
        duration = attributes.get('Duration')
        time_scale = attributes.get('TimeScale')
        is_live = attributes.get('IsLive')
        lookahead_count = attributes.get('LookaheadCount')
        dvr_window_length = attributes.get('DVRWindowLength')

        stream_index_elements = smooth_streaming_media_root.findall('StreamIndex')
        stream_indexes = [StreamIndex.from_xml(stream_index_element) for stream_index_element in stream_index_elements]

        return cls(major_version,
                   minor_version,
                   duration,
                   time_scale,
                   is_live,
                   lookahead_count,
                   dvr_window_length,
                   stream_indexes)
