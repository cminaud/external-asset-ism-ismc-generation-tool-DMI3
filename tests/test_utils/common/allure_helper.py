from allure_commons._allure import StepContext

from external_asset_ism_ismc_generation_tool.common import Logger


class Allure:
    logger: Logger = Logger("Allure")

    class Step(StepContext):
        def __init__(self, title):
            super().__init__(title, {})

        def __enter__(self):
            super().__enter__()
            return self

    @classmethod
    def check(cls, condition, msg: str = ""):
        try:
            assert condition, msg
        except AssertionError as err:
            cls.logger.error(msg)
            raise err
