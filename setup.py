#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='pydata_shiv',
    author="Daniel Roythorne",
    author_email='droythorne@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
    description="Demonstration of using shiv and Docker to make a simple service serving predicitons over grpc.",
    entry_points={
        'console_scripts': [
            'pydata_shiv_server=pydata_shiv.server:main_entrypoint',
            'pydata_shiv_client=pydata_shiv.client:main_entrypoint'
        ],
    },
    install_requires=[
       'grpclib',
       'grpcio',
       'h2',
       'protobuf'
    ],
    license="MIT",
    keywords='shiv docker grpc pydata',
    packages=find_packages(),
    url='https://github.com/drjroythorne/pydata-shiv',
    version='0.0.1' #Modify with bumpversion
)
