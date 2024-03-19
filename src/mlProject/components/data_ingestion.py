import os 
import urllib.request as request
import zipfile
from pathlib import Path 
from src.mlProject.utils.common import get_size
from src.mlProject.entity.config_entity import DataIngestionConfig
from src.mlProject import logger 

class DataIngestion:

    def __init__(self,config:DataIngestionConfig) -> None:
        self.config = config 

    def download_file(self):

        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url=self.config.source_url,
                filename=self.config.local_data_file
            )

            logger.info(f' {filename} downloaded! with the following infor \n{header}')
        else:
            _, filename = os.path.split(self.config.local_data_file)
            logger.info(f' {filename} already exists with size of {get_size(Path(self.config.local_data_file))} ')
    
    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        _, filename = os.path.split(self.config.local_data_file)
        if os.path.exists(self.config.local_data_file):
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_file :
                zip_file.extractall(unzip_path)
                logger.info(f' {filename} unziped inside the {Path(self.config.unzip_dir)}')
        else:
            logger.info(f' data {filename} dose not exists in  {Path(self.config.local_data_file)}')

