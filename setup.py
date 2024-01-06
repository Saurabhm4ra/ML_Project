from setuptools import setup
from typing import List

#Declaring variables for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Saurabh Mehra"
DESCRIPTION = "This is the first machine learning project"
PACKAGES = ["housing"]
REQUIREMENTS_FILE_NAME = "requirements.txt"


def get_requirements_list() -> List[str]:
    '''Description: This function is going to return list of requirement mention in requirements.txt file
    
    return - This function is going to return a list which contain name of libraries mentioned in requirements.txt'''
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()


setup(
name =PROJECT_NAME,
version = VERSION,
author = AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requirements= get_requirements_list()
)

