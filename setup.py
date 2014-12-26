from __future__ import unicode_literals

from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(name='envconf',
      version='0.0.1',
      description='Simple configuration of OS environment variables',
      long_description=long_description,
      classifiers=[],
      keywords='',
      author='Jacob Wasserman',
      author_email='jwasserman@gmail.com',
      url='https://github.com/jwass/envconf',
      license='MIT',
      py_modules=['envconf'],
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'test': ['pytest'],
      },
)