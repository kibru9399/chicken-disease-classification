import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file

    Args:
        path_to_yaml(str): path like input

    Raises:
        ValueError: when yaml file is empty
        e: empty file
    Return:
        ConfigBox: ConfigBox type that contain the configaration file(yaml file)

    

    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f'yaml file: {path_to_yaml} is loaded succesfully.')
            return ConfigBox(content)
    except BoxValueError :
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """ create multiple directories

    Arguments:
        path_to_directories(list): list of directories to be created
        verbose(bool): whether to show log of directory creation, can be ignored if list of directories is long
            
    """
    for path in path_to_directories:
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f'Created a directory at: {path}')
        
@ensure_annotations
def save_json(path: Path, data: dict):
    """ save data as json object
    Arguments:
    path(Path): the path to save the json object at
    data(dict): data to be saved in json
       
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    logger.info(f'json file save at: {path}')
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """ loads json object from a path
    Arguments:
        path(Path): a path from which to read the json object
    Returns:
        ConfigBox: a ConfigBox of the object
    
    """
    with open(path) as f:
        data = json.load(f)
    logger.info(f'succesfully loaded json file from: {path}')
    return ConfigBox(data)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """saves data into a binary format by serializing
    Arguments:
        data(any): the data to be saved
        path(Path): the path to save the file at
    
    """

    joblib.dump(data, path)
    logger.info(f"saved the data as a binary file at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any :
    """loads a binary file
    Arguments:
        path(Path): location to the binary file

    Returns:
        the object stored at the locaiton
    """

    content = joblib.load(path)
    logger.info(f'succesfully loaded the binary file from: {path}')

    return content
@ensure_annotations
def get_size(path: Path) -> str:
    """gets the size of the object at the location
    Arguments:
        path(Path): Path to the file
    Returns:
        size of the file in KB as a string
    
    """
    size = (os.path.getsize(path)/1024)

    return f'~{size} KB'

def encodeImageIntoBase64(croppedImagePath: Path):
    """encode the binary data of the image as a string(commomly used for transfer over HTTP and email)
    Arguments:
        croppedImagePath(Path): location to the image to be encoded
    Returns:
        a byte object as a string
    """
    with open(croppedImagePath, 'rb') as image:
        return base64.b64encode(image.read())
    
def decodeImage(imgString, filename):
    """decode the string into byte and save it to filename
    Arguments:
        imgString(str): string that was encoded to base64
        filename: filename to write the bytes converted from the string
        
    """
    imgdata = base64.b64decode(imgString)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()
