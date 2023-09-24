from src.Risk_Analysis.Pipeline.data_ingestionPipeline import DataIngestionPipeline
from src.Risk_Analysis.Pipeline.data_transformationPipline import DataTransformationPipeline
from src.Risk_Analysis import logger


try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logger.info("Data ingestion completed")

except Exception as e:
    raise e

try:
    data_ingestion=DataTransformationPipeline()
    data_ingestion.main()
    logger.info("Data transformation completed")

except Exception as e:
    raise e

