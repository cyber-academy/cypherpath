import cypherpath
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='cypherpath',
    version=cypherpath.__version__,
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'requests>=2.18.4,<3',
    ],
    license='GNU General Public License v3 (GPLv3)',
    description='',
    long_description=README,
    url='https://github.com/cyber-academy/cypherpath',
    author="Craig Stevenson",
    author_email='craig@cyberacademy.us',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
	'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
