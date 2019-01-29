# Note that without the find_packages the sub package would not be found.

from setuptools import setup, find_packages


setup(name='jason_package',
      packages=find_packages(),
      version='0.1',
      description='Creating a package example.',
      url='http://github.com/jasonbrackman/package_creation',
      author='Jason',
      author_email='asdf@asdf.ca',
      license='MIT',
      zip_safe=True)
