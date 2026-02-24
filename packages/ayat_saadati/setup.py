from setuptools import setup, find_packages
setup(
    name="ayat_saadati",
    version="1.0.0",
    description="Professional toolkit for ayat saadati",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Riley Johnson",
    author_email="ayatsaadat1987@gmail.com",
    url="https://dev.to/ayat_saadat",
    project_urls={
        "Documentation": "https://dev.to/ayat_saadat",
        "Source": "https://dev.to/ayat_saadat",
    },
    packages=find_packages(),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
