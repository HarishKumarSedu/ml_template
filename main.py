from src.mlProject import logger
from src.mlProject.pipeline.stage_01_data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage_02_data_validation_pipeline import DataValidationTrainingPipeline
from src.mlProject.pipeline.stage_03_data_transformation_pipeline import DataTransformationTrainingPipeline
from src.mlProject.pipeline.stage_04_model_trainer_pipeline import ModelTrainerTrainingPipeline



if __name__ == '__main__':
    try:
        STAGE_NAME = 'DATA INGESTION '
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        objDataIngestion = DataIngestionTrainingPipeline()
        objDataIngestion.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

        STAGE_NAME = 'DATA VADLIDATION '
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        objDataValidation = DataValidationTrainingPipeline()
        objDataValidation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

        STAGE_NAME = 'DATA TRANSFORMATION '
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        objDataTransformation = DataTransformationTrainingPipeline()
        objDataTransformation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

        STAGE_NAME = 'MODEL TRAINING '
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        objModelTrain = ModelTrainerTrainingPipeline()
        objModelTrain.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        
    except Exception as e:
        logger.exception(e)
        raise e
