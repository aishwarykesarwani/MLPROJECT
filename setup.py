from setuptools import setup,find_packages

HYPEN_E_DOT='-e .'

from typing import List
def get_requirements(file_path:str)-> List[str]:
    '''
    This function will return list of requirements from file_path file
    ''' 
    requirements=[];
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT);
    return requirements

setup(

    name ="mlproject",
    version="0.0.1",
    author="Aishwary",
    author_email="22ucc012@lnmiit.ac.in",
    packages=find_packages(),

    install_required=get_requirements('requirements.txt')

    ## Manually doing things

    # install_required=['pandas','numpy','seaborn']
)