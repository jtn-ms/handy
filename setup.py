from io import open

from setuptools import find_packages, setup

with open('handy/_version.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'): version = line.strip().split('=')[1].strip(' \'"'); break
    else: version = '0.0.1'

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
            # json or txt f handling        
            "handy = handy.cli.cli:main",
            "delkey = handy.cli.json:delKey",
            "rmempty = handy.cli.json:rmEmpty",
            "beautifyjson = handy.cli.json:rmEmpty",
            "chkey = handy.cli.json:chKey",
            "findkey = handy.cli.json:findKey",
            "repl = handy.cli.text:replace",
            "deline = handy.cli.text:deline",
            # git control
            "version = handy.cli.text:version",
            "commit = handy.cli.git:commit",
            "totalines = handy.cli.text:totalines",
            # frequently-used .bashrc configuration
            "die = handy.cli.simple:shutdown",
            "cls = handy.cli.simple:clear",
            "bashrc = handy.cli.simple:openbashrc",
            "flush = handy.cli.simple:sourcebashrc",
            "chkbashrc = handy.cli.simple:chkbashrc",
            "upload = handy.cli.transfer:upload",
            "download = handy.cli.transfer:download",
            # encrypt part
            "hash = handy.cli.crypt:hash",
            "encode = handy.cli.crypt:Encode",
            "decode = handy.cli.crypt:Decode",
            "encrypt = handy.cli.crypt:Encrypt",
            "decrypt = handy.cli.crypt:Decrypt",
            # filter
            "column = handy.cli.filter:column",
            "row = handy.cli.filter:row",
            "findstr = handy.cli.filter:findstr",
            "extractstr = handy.cli.filter:extractstr",
            "fromstr = handy.cli.filter:fromstr",
            "endstr = handy.cli.filter:endstr",
            "excludestr = handy.cli.filter:excludestr",
            "lenstr = handy.cli.filter:lenstr",
            "upperstr = handy.cli.filter:upperstr",
            "lowerstr = handy.cli.filter:lowerstr",
            # chkinfo
            "dirsize = handy.cli.chkinfo:dirsize",
            "linecount = handy.cli.text:linecount",
            # config
            "replconfkey = handy.cli.config:replconfkey",
            "replconfval = handy.cli.config:replconfval",
            "concatstr = handy.cli.config:concatstr",
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
