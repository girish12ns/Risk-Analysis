from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder,OrdinalEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import pandas as pd
import numpy as np
from src.Risk_Analysis.utils.common import save_oject


class DataTransformation:
    def __init__(self,config):
        self.config=config

    def get_data_transformation(self):

        
        numerical_features=['Term', 'NoEmp', 'NewExist', 'CreateJob', 'RetainedJob', 'UrbanRural','RevLineCr',	
                            'LowDoc', 'DisbursementGross', 'GrAppv', 'SBA_Appv']



        num_pip=Pipeline(steps=[
            ('scaler',StandardScaler()),
            ('imputer',SimpleImputer(strategy='median'))
            ])
        


        
        preprocessor=ColumnTransformer([
            ('num_pip',num_pip,numerical_features)
            ])
        return preprocessor
    
    def data_transformation_initiated(self):

        train_set=pd.read_csv('artifacts\\data_ingestion\\train.csv')

        test_set=pd.read_csv('artifacts\\data_ingestion\\test.csv')

        target_column='MIS_Status'

        x_train,x_test,y_train,y_test=(train_set.drop(target_column,axis=1),
                                      test_set.drop(target_column,axis=1),
                                      train_set[target_column],
                                      test_set[target_column])
        preprocessor=self.get_data_transformation()

        x_train=preprocessor.fit_transform(x_train)
        x_test=preprocessor.transform(x_test)

        save_oject(self.config.preprocessor_dir,preprocessor)

        return x_train,x_test,y_train,y_test