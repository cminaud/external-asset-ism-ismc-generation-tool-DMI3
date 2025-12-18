import xml.etree.ElementTree as ET
from typing import Optional

from external_asset_ism_ismc_generation_tool.common.base_model import BaseModel
from tests.test_utils.ism_manifest_extractor.models.audio import Audio
from tests.test_utils.ism_manifest_extractor.models.text_stream import TextStream
from tests.test_utils.ism_manifest_extractor.models.video import Video


class Body(BaseModel):
    audios: Optional[list]
    videos: Optional[list]
    text_streams: Optional[list]

    def __init__(self, audios: Optional[list] = None, videos: Optional[list] = None, text_streams: Optional[list] = None):
        self.audios = audios
        self.videos = videos
        self.text_streams = text_streams

    @classmethod
    def from_xml(cls, body_element: ET.Element, namespace: dict):
        switch_element = body_element.find(f'{list(namespace.keys())[0]}:switch', namespace)
        audio_elements = switch_element.findall(f'{list(namespace.keys())[0]}:audio', namespace)
        audios = [Audio.from_xml(audio_element, namespace) for audio_element in audio_elements]
        video_elements = switch_element.findall(f'{list(namespace.keys())[0]}:video', namespace)
        videos = [Video.from_xml(video_element, namespace) for video_element in video_elements]
        text_stream_elements = switch_element.findall(f'{list(namespace.keys())[0]}:textstream', namespace)
        text_streams = [TextStream.from_xml(text_stream_element, namespace) for text_stream_element in text_stream_elements]

        return cls(audios, videos, text_streams)
