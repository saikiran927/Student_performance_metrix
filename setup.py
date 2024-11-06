from setuptools import find_packages,setup
from typing import List

hypen_e_dot="-e ."
def get_requirements(file_path:str)->List[str]:
    '''this function will return the list of items'''
    requirment=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[i.replace("\n","") for i in requirments]
        
        if hypen_e_dot in requirments:
            requirments.remove(hypen_e_dot)
    return requirments
    

setup(
    name='mlproject',
    version='0.0.1',
    author='saikiran',
    author_email='bcreddy543@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirments.txt')
) 