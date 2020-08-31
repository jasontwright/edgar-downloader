import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="edgar-downloader",
    version="0.0.1",
    author="Jason Wright",
    author_email="jasontwright@gmail.com",
    description="Download SEC filings from EDGAR using Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jasontwright/edgar-downloader",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)