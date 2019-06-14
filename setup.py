from io import open

from setuptools import find_packages, setup

with open('handy/version.conf', 'r') as f:
    version = '0.0.1'
    for line in f:
        if line.startswith('__version__'): version = line.strip().split('=')[1].strip(' \'"'); break
    
with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

# 'setup.py publish' shortcut.
import sys,os
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()
    
import versioneer

commands = versioneer.get_cmdclass()

packages = ['handi']

REQUIRES = [
            'pysftp>=0.2.9',
            'urllib3<1.23,>=1.21.1',
            'tqdm>=4.19.5',
            'wget>=3.2',
	        'cryptography>=2.1.4',
            'humanize',
            'rlp==0.6.0',
            'cryptography>=2.1.4',
            'nmap>=0.0.1',
            'geocoder>=1.38.1',
            ]

keywords = ['utility','basics']

import config

use_manual_versioning = False

setup(
    name='handi',
    version=version if use_manual_versioning else versioneer.get_version() ,
    description='legacy commands & utils',
    long_description=readme,
    author='gustav0125',
    author_email='gustav0125@outlook.com',
    maintainer='gustav0125',
    maintainer_email='gustav0125@outlook.com',
    url='https://github.com/gustavkkk/handy',
    license='MIT',
    include_package_data=True,
    keywords=keywords,
    
    #package_dir={"": "src"},
    entry_points={
        "console_scripts":config.entry_points
    },   
    
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    #install_requires=REQUIRES,
    extras_require={
    ':sys_platform=="win32"': ["pywin32"],
    "dev": ["mock", "tox", "pyflakes"],
    "dilate": ["noiseprotocol"],
    },
    tests_require=['coverage', 'pytest'],
    zip_safe=False,
    packages=find_packages(),
    package_data={
		  '': ['*.zip','*.py','*.xml','*.rels'],
	},
    cmdclass=commands,
)
