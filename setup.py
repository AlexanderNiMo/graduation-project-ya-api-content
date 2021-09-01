# coding: utf-8

"""
    Read-only API для онлайн-кинотеатра

    Информация о фильмах, жанрах и людях, участвовавших в создании произведения  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "graduation-project-ya-api-content"
VERSION = "1.0.2"
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
    description="Read-only API для онлайн-кинотеатра",
    author_email="",
    url="",
    keywords=["Swagger", "Read-only API для онлайн-кинотеатра"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    Информация о фильмах, жанрах и людях, участвовавших в создании произведения  # noqa: E501
    """
)
