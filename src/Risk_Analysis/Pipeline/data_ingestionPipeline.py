from src.Risk_Analysis.config.configuration import Configuration
from src.Risk_Analysis.components.data_ingestion import DataIngestion


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            data_config=Configuration()
            ingestion_config=data_config.data_ingestion_config()

            data_ingestion=DataIngestion(ingestion_config)
            train_set,test_set=data_ingestion.get_data_ingestion()
        except Exception as e:
            raise e
        
