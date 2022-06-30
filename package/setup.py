from setuptools import setup
from distutils.core import setup

with open('README.md') as f:
    long_description = f.read()

setup(
  name = 'my_hello',         
  packages = ['my_hello'],   
  version = '1.0.0', 
  license='MIT',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Jonathan Guzmán',
  author_email = 'v-jonathangu@microsoft.com',
  url = 'https://github.com/v-jonathangu/pip-package-example',
  #download_url = 'https://github.com/v-jonathangu/pip-package-example/archive/v_0.7.tar.gz',
  keywords = ['sample package', 'azure devops'],
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers', 
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License', 
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)