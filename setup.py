from setuptools import setup

readme = open("./README.md","r")

setup(
      # Basic data for the library.
      name = "PyTesting",
      packages = ['PyTesting'], # The same as "name"
      version = '2.0',
      description = "It's a automatic testing program, for QA.",
      long_description = readme.read(),
      long_description_content_type = 'text/markdown',
      author = 'CyberCoral', # The author
      
      url = "https://github.com/CyberCoral/PyTesting", # The urls
      download_url = "https://github.com/CyberCoral/PyTesting/tarball/2.0",
      
      keywords = ['unit-testing','qa','qa-automation'],
      classifiers = [],
      license = "GPL-3",
      include_package_data = True
      )
