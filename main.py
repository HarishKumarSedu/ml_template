from src.mlProject import logger
from src.mlProject.pipeline.stage_01_dataingestion_pipeline import DataIngestionTrainingPipeline
from src.mlProject.pipeline.stage_02_datavalidation_pipeline import DataValidationTrainingPipeline



if __name__ == '__main__':
    try:
        STAGE_NAME = 'DATA INGESTION '
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

        STAGE_NAME = 'DATA VADLIDATION '
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
        
    except Exception as e:
        logger.exception(e)
        raise e
