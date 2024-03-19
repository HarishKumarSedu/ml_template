### ML Project Template

#### 1. Project Files

`---------------------`

```
project_name = "mlProject"


list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]
```

#### 2. Setup the setuptools for the python package

`--------------------------------------------------`

```
REPO_NAME = 'ml_template'
AUTHOR_USER_NAME = 'HarishKumarSedu'
SRC_REPO = 'mlProject'
AUTHOR_EMAIL = 'harishkumarsedu@gmail.com'

setuptools.setup(

    name= SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='a small pytih ml project for the ml project templet',
    long_description= long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
```

create the seperate version file under the config and enter the version data,
Update the requirements.txt file with packages if you enter `-e` at the end of the requirements .... setuptools automatically install all the packages and setup the python package in `src` folder. 

#### 3. Add The logger function
`-------------------------------`

add the logger function  `src/mlProject/__init__.py` 

```
# setup the loggins string format 
logging_str = "[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"

log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)

    ]
)

logger = logging.getLogger('mlProjectLogger')
```
#### 3. Create Components 
***

*** A. yaml file Constants  ***

    create the constants for the yaml file paths in the project path -> `src/mlProject/Constants/__init__.py`

    ```
    from pathlib import Path

    CONFIG_PATH = Path('config/config.yaml')
    SCHEMA_PATH = Path('schema.yaml')
    PARAMS_PATH = Path('paramas.yaml')
    ```
*** B. Common functions  ***

create common functions to read yaml file, read/write json file...... so on `src/mlProject/utils/common.py`

```
    @ensure_annotations
    def read_yaml(path_to_yaml: Path) -> ConfigBox:
        """reads yaml file and returns
        Args:
            path_to_yaml (str): path like input
        Raises:
            ValueError: if yaml file is empty
            e: empty file
        Returns:
            ConfigBox: ConfigBox type
        """
        try:
            with open(path_to_yaml) as yaml_file:
                content = yaml.safe_load(yaml_file)
                logger.info(f"yaml file: {path_to_yaml} loaded successfully")
                return ConfigBox(content)
        except BoxValueError:
            raise ValueError("yaml file is empty")
        except Exception as e:
            raise e
    @ensure_annotations
    def create_directories(path_to_directories: list, verbose=True):
        """create list of directories
        Args:
            path_to_directories (list): list of path of directories
            ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
        """
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"created directory at: {path}")
    @ensure_annotations
    def save_json(path: Path, data: dict):
        """save json data
        Args:
            path (Path): path to json file
            data (dict): data to be saved in json file
        """
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        logger.info(f"json file saved at: {path}")
    @ensure_annotations
    def load_json(path: Path) -> ConfigBox:
        """load json files data
        Args:
            path (Path): path to json file
        Returns:
            ConfigBox: data as class attributes instead of dict
        """
        with open(path) as f:
            content = json.load(f)
        logger.info(f"json file loaded succesfully from: {path}")
        return ConfigBox(content)
    @ensure_annotations
    def save_bin(data: Any, path: Path):
        """save binary file
        Args:
            data (Any): data to be saved as binary
            path (Path): path to binary file
        """
        joblib.dump(value=data, filename=path)
        logger.info(f"binary file saved at: {path}")
    @ensure_annotations
    def load_bin(path: Path) -> Any:
        """load binary data
        Args:
            path (Path): path to binary file
        Returns:
            Any: object stored in the file
        """
        data = joblib.load(path)
        logger.info(f"binary file loaded from: {path}")
        return data
    @ensure_annotations
    def get_size(path: Path) -> str:
        """get size in KB
        Args:
            path (Path): path of the file
        Returns:
            str: size in KB
        """
        size_in_kb = round(os.path.getsize(path)/1024)
        return f"~ {size_in_kb} KB"
```

*** C. DataClasses  ***

create the Dataclasses for the pipline to validate data parameters 

example : 
```
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path 
    source_url : Path 
    local_data_file: Path 
    unzip_dir: Path
```

*** D. Configuration Manager  ***

```
class ConfigurationManager:

    def __init__(self,
                 config_filepath = CONFIG_PATH,
                 schema_filepath = SCHEMA_PATH,
                 params_filepath = PARAMS_PATH,
                 ) -> None:
        
        self.config = read_yaml(config_filepath) # read the yaml file 
        self.schema = read_yaml(schema_filepath) # read the yaml file 
        self.params = read_yaml(params_filepath) # read the yaml file 

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self)->DataIngestionConfig:

        config = self.config.data_ingestion 
        
        create_directories([config.root_dir])

        data_ingestion = DataIngestionConfig(
            root_dir=config.root_dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,

        )
        return data_ingestion
```

