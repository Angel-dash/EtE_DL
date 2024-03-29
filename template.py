#it will automatically create a folders for me
import os
from pathlib import Path 
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')

project_name='cnnClassifier'

list_of_files=[
    ".github/workflows/.gitkeep",#if you commit empty folder then it will ensuer that is is not empty
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath=Path(filepath)#Path converts linux path to windows path. windows path contains backward slash
    filedir,filename =os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)#creates the directory if it doesn't exist
        logging.info(f"Creating a directory {filedir}for the file :{filename}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info(f"Creating  empyt files : {filepath}")
    else:
        logging.info(f"{filename} is already exists")
