from setuptools import find_packages,setup


setup(
    name='mlproject',
    version='0.0.1',
    author='Pulkit',
    author_email='pulkit.jain8004@thepsi.com',
    packages=find_packages(),
    install_requires=['pandas','numpy','seaborn']
)