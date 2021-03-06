# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "postmark"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Postmark API",
    author_email="",
    download_url = 'https://github.com/jonathan-kosgei/postmark/archive/1.0.tar.gz',
    url="",
    keywords=["Swagger", "Postmark API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Postmark makes sending and receiving email incredibly easy. 
    """
)
