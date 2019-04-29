from io import open

from setuptools import find_packages, setup

with open('handy/_version.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'): version = line.strip().split('=')[1].strip(' \'"'); break
    else:
        version = '0.0.1'

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

# 'setup.py publish' shortcut.
import sys,os
if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

packages = ['handi']

REQUIRES = [
            'pysftp>=0.2.9',
            'urllib3<1.23,>=1.21.1',
            'tqdm>=4.19.5',
            'wget>=3.2',
	        'cryptography>=2.1.4'
            ]

keywords = ''
setup(
    name='handi',
    version=version,
    description='legacy commands & utils',
    long_description=readme,
    author='gustav0125',
    author_email='gustav0125@outlook.com',
    maintainer='gustav0125',
    maintainer_email='gustav0125@outlook.com',
    url='https://github.com/gustavkkk/handy',
    license='MIT',
    include_package_data=True,
    keywords=['utility','basics'],
    
    #package_dir={"": "src"},
    entry_points={
        "console_scripts":
        [
            "gutils = handy.cli.cli:main",
            "delkey = handy.cli.delkey:main",
            "rmempty = handy.cli.rmempty:main",
            "chkey = handy.cli.chkey:main",
            "version = handy.cli.version:main",
            "repl = handy.cli.replace:main",
            "deline = handy.cli.deline:main",
        ]
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

    install_requires=REQUIRES,
    tests_require=['coverage', 'pytest'],
    zip_safe=False,
    packages=find_packages(),
    package_data={
		  '': ['*.zip','*.py'],
	},
)
