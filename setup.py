from setuptools import setup, find_packages

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="Economy.py",
    version="0.0.3",
    author="ErrorTwo",
    author_email="errortwoo@gmail.com",
    description="A package to simply create Economy/Bank",
    long_description="YES",
    long_description_content_type="text/markdown",
    url="https://github.com/ErrorThree/Python-Economy/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
