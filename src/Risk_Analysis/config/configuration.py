from src.Risk_Analysis.entity import DataIngestionConfig,DataTransformationConfig
from src.Risk_Analysis.utils.common import real_yaml,create_directories
from src.Risk_Analysis.constants import config_file,params_file
from src.Risk_Analysis.entity import ModelTrainerConfig



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
    def get_transformations_config(self)->DataTransformationConfig:
        data_trans=self.config.Data_Transformation

        create_directories([data_trans.transformation_dir])

        data_transformation=DataTransformationConfig(
            transformation_dir=data_trans.transformation_dir,
            preprocessor_dir=data_trans.preprocessor_dir
        )

        return data_transformation
    
    def model_trainer_config(self)->ModelTrainerConfig:
        trainer=self.config.Model_Trainer
        transformation=self.config.Data_Transformation
        

        create_directories([trainer.trainer_dir])

        trainer_config=ModelTrainerConfig(
            trainer_dir=trainer.trainer_dir,
            model_dir=trainer.model_dir,
             transformation_dir=transformation.transformation_dir,
            preprocessor_dir=transformation.preprocessor_dir,

            
        )
        return trainer_config