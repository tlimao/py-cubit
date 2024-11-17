from setuptools import setup, find_packages

setup(
    name="pycubit",
    version="0.1.0",
    author="Thiago Lima de Oliveira",
    author_email="tloime@gmail.com",
    description="Cubit pattern for state management in python projects",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/tlimao/py-cubit.git",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
