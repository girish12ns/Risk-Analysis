import os
import pandas as pd
from src.Risk_Analysis.utils.common import load_object
from pathlib import Path


class PredictPipeline:
    def __init__(self):
        pass

    def predict_the_data(self,data):

        model_path=Path('artifacts\model_trainer\model.pkl')
        model=load_object(filepath=model_path)
        preprocessor_path=Path('artifacts\data_transformation\preprocessor.pkl')
        preprocessor=load_object(filepath=preprocessor_path)
        scaled_data=preprocessor.transform(data)
        predict=model.predict(scaled_data)

        return predict






class CustomPipeline:
    def __init__(self,Term:int,NoEmp:int,NewExist:int,CreateJob:int,RetainedJob:int,UrbanRural:int,
                            RevLineCr:int,LowDoc, DisbursementGross:int,GrAppv:int,SBA_Appv:int):
        self.Term=Term,
        self.NoEmp=NoEmp,
        self.NewExist=NewExist,
        self.CreateJob=CreateJob
        self.RetainedJob=RetainedJob,
        self.UrbanRural=UrbanRural
        self.RevLineCr=RevLineCr, 
        self.LowDoc=LowDoc,
        self.DisbursementGross=DisbursementGross, 
        self.GrAppv=GrAppv,
        self.SBA_Appv=SBA_Appv
        


    def get_the_data(self):
        custom_data={
            'Term':self.Term,
             'NoEmp':self.NoEmp,
             'NewExist':self.NewExist,
              'CreateJob':self.CreateJob,
              'RetainedJob':self.RetainedJob,
               'UrbanRural':self.UrbanRural,
               'RevLineCr':self.RevLineCr,
                'LowDoc':self.LowDoc,
                'DisbursementGross':self.DisbursementGross, 
                'GrAppv':self.GrAppv,
                'SBA_Appv':self.SBA_Appv}
         
        
        df=pd.DataFrame(custom_data)
        return df
      



