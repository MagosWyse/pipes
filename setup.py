
from setuptools import setup, find_packages

setup(
    name="peterpiper",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "groq",
        "requests",
        "pyyaml",
    ],
    author="Mr Wyse",
    #author_email="your.email@example.com",
    description="A library for managing pipelines between various generative AI tools",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MagosWyse/pipes.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
