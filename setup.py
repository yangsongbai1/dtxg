#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='dtxg',
    version='1.1',
    description=(
        'Extensions to the dateutil module to support time resolution in multiple languages'
    ),
    long_description=open('README.rst').read(),
    author='yangsongbai',
    author_email='yang18734371940@gmail.com',
    maintainer='yangsongbai',
    maintainer_email='yang18734371940@gmail.com',
    license='BSD License',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/yangsongbai1',
    long_description_content_type = 'text/x-rst',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
    install_requires=[
        'pytz>=2019.1',
        'six>=1.5',
    ]
)