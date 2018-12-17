from setuptools import setup
import os


here = os.path.dirname(__file__)
__version__ = "0.1"
__author__ = "tokoroten"
__author_email__ = "tokoroten@example.com"

def read(name):
    try:
        with open(os.path.join(here, name)) as f:
            return f.read()
    except Exception:
        return ""


setup(
    name="random_forest_contextual_bandit",
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    py_modules=["random_forest_contextual_bandit"],
    description="",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
)
