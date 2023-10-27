from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gue_tools/__init__.py
from gue_tools import __version__ as version

setup(
	name="gue_tools",
	version=version,
	description="GUE Tools",
	author="GUE",
	author_email="cahyadi.suwindra@goapotik.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
