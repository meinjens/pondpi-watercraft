# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pondpi-watercraft',
    version='0.1.0',
    description='PondPi watercraft server',
    long_description=readme,
    author='Jens Meinecke',
    author_email='mail@jensmeinecke.de',
    url='https://github.com/meinjens/pondpi-watercraft',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
