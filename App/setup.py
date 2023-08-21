from setuptools import find_packages, setup
from typing import List

Hypen_e_dot = '-e.'

def get_req(file_path : str) -> List[str]:
    
    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [x.replace("\n", "") for x in req]
        
        if Hypen_e_dot in req:
            req.remove(Hypen_e_dot)
            
    return req

setup(
    name = " ",
    version = "0.0.1",
    author = "pinilDissanayaka",
    author_email = "pinildissanayaka@gmail.com",
    packages = find_packages(),
    install_requires = get_req('requirements.txt')
)

