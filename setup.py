#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="Markdown-Video",
    version="0.1",
    url="http://github.com/Holzhaus/Python-Markdown-Video",
    license="GPL",
    author="Jan Holthuis",
    author_email="jholthuis@mixxx.org",
    description="Video Extension for Markdown",
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Utilities",
    ],
    platforms="any",
    py_modules=["markdown_video"],
    include_package_data=False,
    install_requires=[
        "Markdown",
    ],
)
