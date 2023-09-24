from src.Risk_Analysis.config.configuration import Configuration
from src.Risk_Analysis.components.data_transformation import DataTransformation


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            transformation_config=Configuration()
            config=transformation_config.get_transformations_config()

            data_transformation=DataTransformation(config)
            x_train,x_test,y_test,y_train=data_transformation.data_transformation_initiated()
        except Exception as e:
            raise e