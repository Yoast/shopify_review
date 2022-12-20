# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 20:11:43 2022

@author: Honglei
"""

from setuptools import setup, find_packages

setup(
    name='scrapy shopify review',
    version='0.1.0',
    description='Setting up shopify review',
    author='honglei/yoast',
    author_email='honglei.zhang@yoast.com',
    url='https://blog.godatadriven.com/setup-py',
    packages=find_packages(include=['shopify_review']),
    install_requires=[
        'scrapy'
    ]
)
