from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path=str)->list[str]:
    '''
    This function will return a list of requirements
    '''
    requirements: List[str] = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")

setup(
    name="mlproject",
    version="0.0.1",
    author="manova",
    author_email="manova.abraham@ gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
