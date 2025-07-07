from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

setup(
    name="XRF-SPECS",
    description="TODO add a description",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[],  # TODO specifiy dependencies
)

# TODO specify resources in manifest.ini or with the `data_files` attribute
