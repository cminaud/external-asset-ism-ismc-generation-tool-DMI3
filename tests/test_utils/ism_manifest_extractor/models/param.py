from external_asset_ism_ismc_generation_tool.common import BaseModel


class Param(BaseModel):
    name: str
    value: str
    value_type: str

    def __init__(self, name: str, value: str, value_type: str):
        self.name = name
        self.value = value
        self.value_type = value_type
