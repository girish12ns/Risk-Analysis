from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

class DataIngestion:
    def __init__(self,config):
        self.config=config

    def get_data_ingestion(self):

        df=pd.read_csv(self.config.source_dir)

        train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

        train_set.to_csv(self.config.train_dir,index=False)

        test_set.to_csv(self.config.test_dir,index=False)
    
        return train_set,test_set