from tests.test_utils.ism_manifest_extractor.models.smil import Smil


class IsmManifestExtractor:
    @staticmethod
    def extract(ism_manifest_str: str) -> Smil:
        return Smil.from_xml(ism_manifest_str)


