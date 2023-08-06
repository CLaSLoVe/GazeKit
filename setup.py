from setuptools import find_packages, setup

with open('readme.md') as f:
    long_description = f.read()

setup(
    name='gazekit',
    packages=find_packages(),
    version='0.0.3',
    description='This is a Python library designed for processing eye-tracking data.',
    author='CLaSLoVe',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/CLaSLoVe/GazeKit',
    license='MIT',
    install_requires=["numpy>=1.0", "pandas>=2.0"],
    # setup_requires=['pytest-runner'],
    # tests_require=['pytest==6.2.4'],
    # test_suite='tests',
)