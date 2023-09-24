from src.Risk_Analysis.Pipeline.data_ingestionPipeline import DataIngestionPipeline
from src.Risk_Analysis.Pipeline.data_transformationPipline import DataTransformationPipeline
from src.Risk_Analysis import logger
from src.Risk_Analysis.Pipeline.Model_trainerPipeine import ModelTrainerPipeline


try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logger.info("Data ingestion completed")

except Exception as e:
    raise e

try:
    data_transformation=DataTransformationPipeline()
    data_transformation.main()
    logger.info("Data transformation completed")

except Exception as e:
    raise e

try:
    model_training=ModelTrainerPipeline()
    model_training.main()
    logger.info("Model_training  completed")

except Exception as e:
    raise e

