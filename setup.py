#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='python-jenkins',
      version='0.2',
      description='Python bindings for the remote Jenkins API',
      long_description='Python bindings for the remote Jenkins API',
      author='Ken Conley',
      author_email='kwc@willowgarage.com',
      url='http://launchpad.net/python-jenkins',
      packages=find_packages(),
      package_dir={"jenkins": "jenkins"},
      include_package_data=True,
     )
