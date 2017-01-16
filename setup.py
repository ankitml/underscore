import os
from setuptools import find_packages, setup

#with open(os.path.join(os.path.dirname(__file__), 'djangodeletes/README.rst')) as readme:
#    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='underscore',
    version='0.5',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',  # example license
    description='Python port of underscore.js library',
    long_description='Underscore is a python library that provides a whole mess of useful functional programming helpers without extending any built-in objects. ',
    url='https://github.com/ankitml/underscore',
    author='Ankit Mittal',
    author_email='ankitml@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
