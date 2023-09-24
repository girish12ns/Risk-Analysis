from src.Risk_Analysis.components.data_transformation import DataTransformation
from src.Risk_Analysis.config.configuration import Configuration

from src.Risk_Analysis.components.Model_trainer import ModelTrainer

class ModelTrainerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            trainer=Configuration()
            config=trainer.model_trainer_config()

            transformation=DataTransformation(config)
            x_train,x_test,y_train,y_test=transformation.data_transformation_initiated()

            model_trainer=ModelTrainer(config)
            model=model_trainer.select_best_model(x_train,x_test,y_train,y_test)
        except Exception as e:
            raise e