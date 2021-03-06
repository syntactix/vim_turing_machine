from setuptools import find_packages
from setuptools import setup


setup(
    name='vim-turing-machine',
    version='1.0.0',
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'colored',
    ],
    packages=find_packages(exclude=('tests*', 'testing*')),
)
