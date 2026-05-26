from setuptools import setup, find_packages
setup(
    name="ayatsaadati",
    version="1.0.0",
    description="Professional toolkit for ayatsaadati",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Drew Martinez",
    author_email="ayatsaadat1987@gmail.com",
    url="https://qamar.website",
    project_urls={
        "Documentation": "https://qamar.website",
        "Source": "https://qamar.website",
    },
    packages=find_packages(),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
