import os 
import sys
import logging 

#module will replace the file which we are running. If we are runnig template.py then it will log we are running template.py
logging_str="[%(asctime)s:%(levelname)s: %(module)s: %(message)s]"

#creating a seperate folder for keeping the logs
log_dir="logs"
log_filepath=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,

    handlers=[
        logging.FileHandler(log_filepath),#adding the log on the folder
        logging.StreamHandler(sys.stdout)#printing the log on my terminal
    ]


)
logger=logging.getLogger("cnnClassifierLogger")