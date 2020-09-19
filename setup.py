from setuptools import setup
import re

with open('schoolpy/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

requirements = []
try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    pass

with open("README.md", "r") as f:
    readme = f.read()

setup(name="schoolpy",
      packages=["schoolpy"],
      author="12944qwerty",
      version=version,
      description="A package schools could use to manage their DB",
      long_description=readme,
      long_description_content_type="text/markdown",
      install_requires=requirements,
      python_requires=">=3.6",
      url="https://github.com/12944qwerty/schoolpy",
      classifiers=[
          "Development Status :: 2 - Pre-Alpha",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3.8",
          "Topic :: Education",
          "Topic :: Education :: Computer Aided Instruction (CAI)"
        ],
)
