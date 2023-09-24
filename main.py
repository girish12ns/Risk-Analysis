from src.Risk_Analysis.Pipeline.data_ingestionPipeline import DataIngestionPipeline
from src.Risk_Analysis import logger


try:
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logger.info("Data ingestion completed")

except Exception as e:
    raise e
