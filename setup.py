"""Setup script for jinja_datatables"""

import os.path
from setuptools import setup, find_packages

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="jinja_datatables",
    version="0.0.1",
    description="Python library that helps create searchable, custom filterable datatables",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/theheuman/jinja-datatables",
    author="TheHeuman",
    author_email="jacob.heuman@aciwebs.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(exclude=("tests", "dist")),
    include_package_data=True,
    install_requires=[
        "Jinja2",
    ],
)
