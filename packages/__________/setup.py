from setuptools import setup, find_packages
setup(
    name="خانه_باتری",
    version="1.0.0",
    description="Professional toolkit for خانه باتری",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Drew Martinez",
    author_email="ayatsaadat1987@gmail.com",
    url="https://www.batteries.ir/",
    project_urls={
        "Documentation": "https://www.batteries.ir/",
        "Source": "https://www.batteries.ir/",
    },
    packages=find_packages(),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
