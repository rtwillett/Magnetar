import setuptools

with open("README.md", "r") as f: 
        long_description = f.read()

setuptools.setup(
    name="magnetar",
    version="0.0.1",
    author="Ryan Willett",
    author_email="ryan.willett@gmail.com",
    description="Datamining library",
    long_description="long_description",
    url="https://github.com/rtwillett/Magnetar",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
        ],
    install_requires=[
        "wheel",
        "jupyter",
        "pandas",
        "numpy"
        ]
    )
