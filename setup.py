from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in anfaceducation/__init__.py
from anfaceducation import __version__ as version

setup(
	name="anfaceducation",
	version=version,
	description="Anfac Education is app for education",
	author="Anfac Tech",
	author_email="info@anfactech.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
