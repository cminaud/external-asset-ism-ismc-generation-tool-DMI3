from tests.test_utils.ismc_manifest_extracror.models.smooth_streaming_media import SmoothStreamingMedia


class IsmcManifestExtractor:
    @staticmethod
    def extract(ismc_manifest_str: str) -> SmoothStreamingMedia:
        return SmoothStreamingMedia.from_xml(ismc_manifest_str)


