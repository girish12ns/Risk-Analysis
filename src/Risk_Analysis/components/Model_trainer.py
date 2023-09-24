import pandas as pd
import numpy as np
from src.Risk_Analysis.utils.common import save_oject,model_eval

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from xgboost import XGBRFClassifier
from catboost import CatBoostClassifier
from src.Risk_Analysis.utils.common import model_eval

class ModelTrainer:
    def __init__(self,config):
        self.config=config

    def get_model_trainer(self,x_train,x_test,y_train,y_test):

        models={'logistic_model':LogisticRegression(),
                'Naie_bayes_model':GaussianNB(),
                'K_Neighbors_model':KNeighborsClassifier(),
                'Decision_tree_model':DecisionTreeClassifier(),
                'Random_forest':RandomForestClassifier(),
                'GradientBoostingClassifier':GradientBoostingClassifier(),
                'xgboost':XGBRFClassifier(),
                'cat_boost':CatBoostClassifier()}
        
        recall_score_list=[]
        accuracy_score_list=[]
        model_list=[]
        for i in range(len(list(models))):
            model=list(models.values())[i]
            model.fit(x_train,y_train)

            predict=model.predict(x_test)

            score,recall=model_eval(y_test,predict)

            model_list.append(list(models.keys())[i])

            accuracy_score_list.append(score)
            recall_score_list.append(recall)
       
        return (recall_score_list,models,model_list)
    
    def select_best_model(self,x_train,x_test,y_train,y_test):
        report={}

        recall_score_list,models,model_list=self.get_model_trainer(x_train=x_train,x_test=x_test,y_train=y_train,y_test=y_test)

        for key,value in zip(model_list,recall_score_list):
            report[key]=value

        sorted_model=sorted(report.items(),key=lambda x:x[1],reverse=True)
        

        model=sorted_model[0][0]

        best_recall_score=sorted_model[0][1]

        best_model=models[model]

        save_oject(filepath=self.config.model_dir,obj=best_model)

        print(best_recall_score)
        