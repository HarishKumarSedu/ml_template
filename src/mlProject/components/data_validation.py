import os 
from src.mlProject import logger
from src.mlProject.entity.config_entity import DataValidationConfig
import pandas as pd 

class DataValidation:

    def __init__(self,config:DataValidationConfig) -> None:
        self.config = config

    def validate_all_columns(self)->bool:
        try :
            validtion_staus = None 

            data = pd.read_csv(self.config.unzip_data_dir)
            all_cols = data.columns.to_list()

            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validtion_staus = False
                    with open(self.config.STATUS_FILE, 'w') as file :
                        file.write(f'Validation status: {validtion_staus}')
                else:
                    validtion_staus = True
                    with open(self.config.STATUS_FILE, 'w') as file :
                        file.write(f'Validation status: {validtion_staus}')
            return validtion_staus

        except Exception as e:
            raise e 