import os 
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


project_name="Risk_Analysis"

file_name_list=[
    "github/workflows/.gitkeep",
    "src/{}/__init__.py".format(project_name),
    "src/{}/components/__init__.py".format(project_name),
    "src/{}/utils/__init__.py".format(project_name),
    "src/{}/config/__init__.py".format(project_name),
    "src/{}/config/configuration".format(project_name),
    "src/{}/Pipeline/__init__.py".format(project_name),
    "src/{}/entity/__init__.py".format(project_name),
    "src/{}/utils/common.py".format(project_name),
    "src/{}/constants/__init__.py".format(project_name),
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "research/trials.ipynb",
    "templates/index.html",
    "setup.py"]

for file in file_name_list:
    file_path=Path(file)
    dir_file,file_name=os.path.split(file_path)

    if dir_file!="":
        logging.info("The directories are created")
        os.makedirs(dir_file,exist_ok=True)

    if not os.path.exists(file_path):

        with open(file_path,'w') as f:
            logging.info("files  are created")


