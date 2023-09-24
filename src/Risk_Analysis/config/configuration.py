from src.Risk_Analysis.entity import DataIngestionConfig
from src.Risk_Analysis.utils.common import real_yaml,create_directories
from src.Risk_Analysis.constants import config_file,params_file


class Configuration:
    def __init__(self,config=config_file,params=params_file):
        self.config=real_yaml(config)
        self.params=real_yaml(params)
        create_directories([self.config.Artifacts])

    def data_ingestion_config(self)->DataIngestionConfig:
        data_ingestion=self.config.Data_Ingestion
        create_directories([data_ingestion.root_dir])

        data_ingestion_config=DataIngestionConfig(
            root_dir=data_ingestion.root_dir,
            source_dir=data_ingestion.source_dir,
            train_dir=data_ingestion.train_dir,
            test_dir=data_ingestion.test_dir
  
        )
        return data_ingestion_config