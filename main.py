from src.mlProject import logger
from src.mlProject.pipeline.stage_01_dataingestion_pipeline import DataIngestionTrainingPipeline



if __name__ == '__main__':
    try:
        STAGE_NAME = 'DATA INGESTION '
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
