
from setuptools import setup

setup(
    name = "dbwrapper",
    version = "0.1-prealpha",
    author = "Austin Zalac",
    description = ("Wraps SQL Syntax into a python API."),
    packages=[
        'dbwrapper',
        'dbwrapper.sqlite',
        'dbwrapper.postgresql'
    ],
    long_description=None,
    # install_requires = [
    #     "psycopg2"
    # ]
    extras_require={
        "postgres": ["psycopg2"]
    }
)