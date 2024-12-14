from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT = '-e .'

#defining the get_requirements funtion
def get_requirements(file_path:str)->List[str]:
    '''
    this will return the list of requirements
    '''
    requirements =[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        #this function will repalce \n with blank space in newline
        requirements = [req.replace("\n"," ") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name = 'Vijay Kumar',
version = '0.0.1',
author = 'Vijay',
author_email='vvrkumar0122@gmai.com', 
packages = find_packages(),
#As we cannot put all out Lib as so we use a function that takes values from requirements.txt 
install_requires =get_requirements('requirements.txt')

)