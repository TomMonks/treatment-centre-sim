import setuptools
from setuptools.command.egg_info import egg_info
from treat_sim import __version__

class egg_info_ex(egg_info):
    """Includes license file into `.egg-info` folder."""

    def run(self):
        # don't duplicate license into `.egg-info` when building a distribution
        if not self.distribution.have_run.get('install', True):
            # `install` command is in progress, copy license
            self.mkpath(self.egg_info)
            self.copy_file('LICENSE', self.egg_info)

        egg_info.run(self)


# Read in the requirements.txt file
with open("requirements.txt") as f:
    requirements = []
    for library in f.read().splitlines():
        requirements.append(library)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="treat-sim",
    version=__version__,
    author="Thomas Monks",
    # I've created a specific email account before and forwarded to my own.
    author_email="forecast-tools@gmail.com",
    license="The MIT License (MIT)",
    license_files=('LICENSE', ),
    description="A free and open implementation of the Treatment Centre Model from Nelson (2013)",
    # read in from readme.md and will appear on PyPi
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TomMonks/treatment-centre-sim",
    packages=setuptools.find_packages(),
    # if true look in MANIFEST.in for data files to include
    include_package_data=True,
    # these are for documentation 
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8.12',
    install_requires=requirements,
)