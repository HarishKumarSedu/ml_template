from src.mlProject.entity.config_entity import (DataIngestionConfig,
                                                DataValidationConfig,
                                                DataTransformationConfig,
                                                ModelTrainConfig
                                                )
from src.mlProject import logger
from src.mlProject.constants import *
from src.mlProject.utils.common import read_yaml, create_directories, get_size

class ConfigurationManager:

    def __init__(self,
                 config_filepath = CONFIG_PATH,
                 schema_filepath = SCHEMA_PATH,
                 params_filepath = PARAMS_PATH,
                 ) -> None:
        
        self.config = read_yaml(config_filepath) # read the yaml file 
        self.schema = read_yaml(schema_filepath) # read the yaml file 
        self.params = read_yaml(params_filepath) # read the yaml file 

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:

        config = self.config.data_ingestion 
        
        create_directories([config.root_dir])
        data_ingestion = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )
        return data_ingestion
    
    def get_data_validation_config(self)->DataValidationConfig:
        config = self.config.data_validation 
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation = DataValidationConfig(
            root_dir        =config.root_dir,
            unzip_data_dir  =config.unzip_data_dir,
            STATUS_FILE     =config.STATUS_FILE,
            all_schema      =schema
        )
        return data_validation

    def get_data_transformation_config(self)-> DataTransformationConfig:
        
        config = self.config.data_transfromation
        create_directories([config.root_dir])
        
        data_transformation = DataTransformationConfig(
            root_dir= config.root_dir,
            data_path= config.data_path
        )
        return data_transformation
    
    def get_model_trainer_config(self)->ModelTrainConfig:
        config = self.config.model_trainer
        target = self.schema.TARGET_COLUMN
        params = self.params.ElasticNet
        create_directories([config.root_dir])
        
        model_trainer = ModelTrainConfig(
                    root_dir            = config.root_dir  ,
                    train_data_path     = config.train_data_path,
                    test_data_path      = config.test_data_path,
                    model_name          = config.model_name,
                    alpha               = params.alpha,
                    l1_ratio            = params.l1_ratio,
                    target_column       = target.name,
        )
        
        return model_trainer