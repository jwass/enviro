from __future__ import unicode_literals

from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='enviro',
      version='0.0.2',
      description='Simple configuration of OS environment variables',
      long_description=long_description,
      classifiers=[],
      keywords='',
      author='Jacob Wasserman',
      author_email='jwasserman@gmail.com',
      url='https://github.com/jwass/enviro',
      license='MIT',
      py_modules=['enviro', 'enviro_ipy_ext'],
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'test': ['pytest'],
      },
)
