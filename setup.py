"""Setup script for jinja_datatables"""

import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="jinja_datatables",
    version="0.0.8",
    description="Python library that helps create searchable, custom filterable datatables",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/theheuman/jinja-datatables",
    author="TheHeuman",
    author_email="jacob.heuman@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    package_data={'': ['*.html', '*.js']},
    include_package_data=True,
    packages=find_packages(exclude=["tests", "examples"]),
    install_requires=[
        "Jinja2",
    ],
)
