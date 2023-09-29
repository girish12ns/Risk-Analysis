import os
from box.exceptions import BoxValueError
import yaml
from src.Risk_Analysis import logger
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import dill

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier,GradientBoostingClassifier
from xgboost import XGBRFClassifier
from catboost import CatBoostClassifier
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix,recall_score





@ensure_annotations
def real_yaml(path_to_yaml:Path)->ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content =yaml.safe_load(yaml_file)
        return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(file:list,verbose=True):
    '''creating the directored'''
    for path in file:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info("directory is created ")



def save_oject(filepath,obj):
    filepath=Path(filepath)
    
    with open(filepath, 'wb') as f:
        load_obj=dill.dump(obj, f)


def model_eval(true,prediction):
    score=accuracy_score(true,prediction)
    recall=recall_score(true,prediction)
    return (score,recall)

def load_object(filepath):

    with open(filepath,'rb') as f:
        loaded_object = dill.load(f)
    return loaded_object




    
