from setuptools import setup, find_packages
setup(
    name="یونیت_اپ",
    version="1.0.0",
    description="Professional toolkit for یونیت اپ",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Morgan Davis",
    author_email="ayatsaadat1987@gmail.com",
    url="https://www.younit-app.com/",
    project_urls={
        "Documentation": "https://www.younit-app.com/",
        "Source": "https://www.younit-app.com/",
    },
    packages=find_packages(),
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
