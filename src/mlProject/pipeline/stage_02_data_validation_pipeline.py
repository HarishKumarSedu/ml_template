from src.mlProject import logger
from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.components.data_validation import DataValidation

STAGE_NAME = 'Data Validation'

class DataValidationTrainingPipeline:

    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()