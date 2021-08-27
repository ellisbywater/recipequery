from setuptools import setup

setup(name='python_kroger_client',
      version='0.1',
      description="Wrapper around Kroger's api",
      url='http://github.com/ellisbywater/python-kroger-client',
      author='ellisbywater',
      license='MIT',
      packages=['python_kroger_client'],
      install_requires=[
          'simple_cache',
          'selenium',
      ],
      zip_safe=False)