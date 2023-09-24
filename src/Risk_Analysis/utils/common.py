import os
from box.exceptions import BoxValueError
import yaml
from src.Risk_Analysis import logger
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

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






    
