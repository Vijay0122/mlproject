import os 
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

#Make sure you have installed Scikit learn
from sklearn.model_selection import train_test_split
# Used to creat class variables
from dataclasses import dataclass

#inputs given to data ingestion components 
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifacts',"train.csv")
    test_data_path: str = os.path.join('artifacts',"test.csv")
    raw_data_path: str = os.path.join('artifacts',"raw.csv")



class DataIngestion:
    def __init__(self):
        #this ingestion_config will consist the above three inputs 
        self.ingestion_config = DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info('Read the Dataset as Dataframe')
            #making the files to save the data in ingestion and also if it is their then we don't rewrite (exit_ok func)
            #and also giving the dir name 
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            #Saving it with raw datapath 
            df.to_csv(self.ingestion_config.raw_data_path, index=False,header=True)

            logging.info('Train Test split has initiated')

            train_set,test_set = train_test_split(df, test_size = 0.2, random_state=42)
            #Saving it in artifact folder 
            train_set.to_csv(self.ingestion_config.train_data_path, index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path, index=False,header=True)

            logging.info("Ingestion of the data is completed")

            #Returning the data into the next part that is Data Transformation
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="main":
    obj = DataIngestion()
    obj.initiate_data_ingestion()

  