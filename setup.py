from setuptools import setup, find_packages
from typing import List


HYPHEN_E_DOT = "-e ."
# This function will read the requirements.txt file and return a list of requirements(packages)
def get_requirements(file_path) ->List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements


setup(
    name="ML Project 01",
    version="0.0.1",
    author="Uzair Khan",
    author_email="uzairkhaan2003@gmail.com",
    packages=find_packages(),
    install_requires=[
        # "pandas","numpy","seaborn"
        get_requirements("requirements.txt")
    ]
)