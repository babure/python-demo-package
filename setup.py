# setup.py

from setuptools import setup, find_packages

setup(
    name='myorg_connectors',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'elasticsearch==7.12.0',
        'pymongo==3.13',
    ],
)
