import xml.etree.ElementTree as ET
from typing import Optional

from external_asset_ism_ismc_generation_tool.common.base_model import BaseModel


class QualityLevel(BaseModel):
    index: str
    bitrate: str
    buffer_time: Optional[str]
    nominal_bitrate: Optional[str]
    hardware_profile: Optional[str]
    codec_private_data: str = "0"
    sampling_rate: Optional[str]
    max_height: Optional[str]
    max_width: Optional[str]
    channels: Optional[str]
    bits_per_sample: Optional[str]
    packet_size: Optional[str]
    audio_tag: Optional[str]
    four_cc: Optional[str]
    nal_unit_length_field: Optional[str]

    def __init__(self, index: str,
                 bitrate: str,
                 buffer_time: Optional[str] = None,
                 nominal_bitrate: Optional[str] = None,
                 hardware_profile: Optional[str] = None,
                 codec_private_data: str = "0",
                 sampling_rate: Optional[str] = None,
                 max_height: Optional[str] = None,
                 max_width: Optional[str] = None,
                 channels: Optional[str] = None,
                 bits_per_sample: Optional[str] = None,
                 packet_size: Optional[str] = None,
                 audio_tag: Optional[str] = None,
                 four_cc: Optional[str] = None,
                 nal_unit_length_field: Optional[str] = None):
        self.index = index
        self.bitrate = bitrate
        self.buffer_time = buffer_time
        self.nominal_bitrate = nominal_bitrate
        self.hardware_profile = hardware_profile
        self.codec_private_data = codec_private_data
        self.sampling_rate = sampling_rate
        self.max_height = max_height
        self.max_width = max_width
        self.channels = channels
        self.bits_per_sample = bits_per_sample
        self.packet_size = packet_size
        self.audio_tag = audio_tag
        self.four_cc = four_cc
        self.nal_unit_length_field = nal_unit_length_field

    @classmethod
    def from_xml(cls, quality_level_element: ET.Element):
        attributes = quality_level_element.attrib
        index = attributes.get('Index')
        bitrate = attributes.get('Bitrate')
        buffer_time = attributes.get('BufferTime')
        nominal_bitrate = attributes.get('NominalBitrate')
        hardware_profile = attributes.get('HardwareProfile')
        codec_private_data = attributes.get('CodecPrivateData')
        sampling_rate = attributes.get('SamplingRate')
        max_height = attributes.get('MaxHeight')
        max_width = attributes.get('MaxWidth')
        channels = attributes.get('Channels')
        bits_per_sample = attributes.get('BitsPerSample')
        packet_size = attributes.get('PacketSize')
        audio_tag = attributes.get('AudioTag')
        four_cc = attributes.get('FourCC')
        nal_unit_length_field = attributes.get('NALUnitLengthField')

        return cls(index,
                   bitrate,
                   buffer_time,
                   nominal_bitrate,
                   hardware_profile,
                   codec_private_data,
                   sampling_rate,
                   max_height,
                   max_width,
                   channels,
                   bits_per_sample,
                   packet_size,
                   audio_tag,
                   four_cc,
                   nal_unit_length_field)
