import os
from setuptools import setup

# read the long description
with open('readme.md', 'r') as f:
    long_description = f.read()

# read the version
version_info = {}
with open(os.path.join('di2008', 'version.py')) as f:
    exec(f.read(), version_info)
__version__ = version_info['__version__']

# read the requirements.txt

setup_attributes = {
    'name': 'di2008',
    'version': __version__,
    'description': 'Object-oriented API for DATAQ DI-2008',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
    'url': 'https://github.com/slightlynybbled/di2008',
    'author': 'Jason R. Jones',
    'author_email': 'slightlynybbled@gmail.com',
    'license': 'MIT',
    'packages': ['di2008'],
    'python_requires': '>=3.6.0',
    'setup_requires': ['pyusb>=1.0.0'],
    'install_requires': ['pyusb>=1.0.0'],
    'classifiers': [
        'License :: OSI Approved :: MIT License',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    'zip_safe': False
    
}

setup(**setup_attributes)
