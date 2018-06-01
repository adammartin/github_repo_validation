#!/usr/bin/env python3
import os.path
from setuptools import setup, find_packages
from glob import glob

setup(
    name='github_repo_validation',
    description='',
    url='',

    author='HI Digital Solutions, LLC',
    author_email='support@hidigitalsolutionsllc.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    packages=find_packages('src'),
    package_dir={'': 'src'},
    entry_points='''
            [console_scripts]
            github_repo_validation=github_repo_validation.cli:repo_consistency_report
    ''',

    install_requires=[
        'click'
    ]
)
