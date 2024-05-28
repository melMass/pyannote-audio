from setuptools import setup, find_packages
from pathlib import Path


def read_version():
    here = Path(__file__).parent
    version = (here / "version.txt").read_text().strip()

    tmp = f"__version__ = version = '{version}'"
    (here / "pyannote" / "audio" / "version.py").write_text(tmp)

    return version


setup(version=read_version(), packages=find_packages())
