from setuptools import setup, find_packages
import sys, os

version = '1.1'

setup(
    name='ckanext-oaipmh-dc',
    version=version,
    description="OAI-PMH Harvester for Dublin Core Metadata",
    long_description="",
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='Liip AG',
    author_email='ogd@liip.ch',
    url='http://www.liip.ch',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=\
    """
    [ckan.plugins]
    oaipmh_dc_harvester=ckanext.oaipmh.harvester:OaipmhDCHarvester
    """,
)
