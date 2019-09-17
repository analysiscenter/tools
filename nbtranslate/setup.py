"""
NBTranslate translates jupyter notebook cells markdown cells into Russian.
"""
import re
from setuptools import setup, find_packages


VERSION = 0.1

with open('README.md', 'r') as f:
    long_description = f.read()


setup(
    name='nbtranslate',
    packages=find_packages(),
    version=VERSION,
    url='https://github.com/analysiscenter/tools',
    license='Apache License 2.0',
    author='Roman Kh at al',
    author_email='rhudor@gmail.com',
    description='NBConvert exporter to translate markdown cells into Russian',
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    platforms='any',
    install_requires=[
        'nbconvert>=5.6.0',
        'jupyter-contrib-nbextensions>=0.5.1',
        'google-cloud-translate==1.6.0',
    ],
    entry_points = {
        'nbconvert.exporters': [
            'nbtru = nbtranslate:TranslateExporter',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering'
    ],
)
