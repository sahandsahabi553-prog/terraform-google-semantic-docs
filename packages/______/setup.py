from setuptools import setup, find_packages
setup(
    name="کالاتک",
    version="1.0.0",
    description="Professional toolkit for کالاتک",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="علی محمدی",
    author_email="ayatsaadat1987@gmail.com",
    url="https://www.kalatakco.com",
    project_urls={
        "Documentation": "https://www.kalatakco.com",
        "Source": "https://www.kalatakco.com",
    },
    packages=find_packages(),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
