from io import open

from setuptools import find_packages, setup

with open('handy/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.0.1'

with open('README.rst', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = [
            'pysftp>=0.2.9',
            'urllib>=1.22',
            'urllib3>=1.21.1,<1.23',
            ]

setup(
    name='handy',
    version=version,
    description='',
    long_description=readme,
    author='gustavkkk',
    author_email='gustav0125@outlook.com',
    maintainer='gustavkkk',
    maintainer_email='gustav0125@outlook.com',
    url='https://github.com/gustavkkk/handy',
    license='MIT/Apache-2.0',

    keywords=[
        '',
    ],

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
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

    packages=find_packages(),
)
