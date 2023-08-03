from setuptools import find_packages, setup

setup(
    name='gazekit',
    packages=find_packages(),
    version='0.1.0',
    description='This is a Python library designed for processing eye-tracking data. It includes functions for noise reduction, area of interest (AOI) localization, data analysis, and plotting. With this library, you can easily preprocess and analyze eye-tracking data to gain insights into human visual cognitive processes. Whether you are conducting research in psychology, neuroscience, or human-computer interaction, this library can help you streamline your data processing workflow and obtain more accurate and reliable results.',
    author= 'CLaSLoVe',
    license='MIT',
    install_requires=["numpy>=1.0", "pandas>=2.0"],
    # setup_requires=['pytest-runner'],
    # tests_require=['pytest==6.2.4'],
    # test_suite='tests',
)