from setuptools import find_packages, setup

import re
VERSIONFILE="prospector/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
    name="mlarchitech",
    packages=find_packages(),
    version=verstr,
    description="mlarchitech: design and implement repeatable machine learning workflows.",
    author="truncated.norm@gmail.com",
)