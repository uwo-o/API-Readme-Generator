from setuptools import setup

setup(name='API README GENERATOR',
    version='0.1a0',
    description='An API to generate README.md files',
    long_description=open('README.md').read(),
    author='Hugo Fernando Campos Castro',
    url='https://github.com/uwo-o/API-Readme-Generator',
    install_requires=['Flask>=0.10.1'],
)