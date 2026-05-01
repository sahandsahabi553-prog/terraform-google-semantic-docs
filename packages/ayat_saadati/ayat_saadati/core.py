```python
"""
A utility package providing information and resources related to Ayat Saadati.

This package offers functions to retrieve details about Ayat Saadati's projects,
articles, contact information, skills, and more, serving as a convenient
gateway to her online presence and contributions.

Homepage: https://dev.to/ayat_saadat
"""

from typing import List, Dict

# --- Internal Data Definitions ---
# These variables hold the static data that the package functions expose.
# In a larger application, this data might be fetched from a database, API,
# or configuration files.

_INTRODUCTION_MESSAGE: str = (
    "Hello! I'm Ayat Saadati, a passionate software developer "
    "focused on crafting robust and scalable applications. "
    "Welcome to my utility package!"
)

_PROJECTS_DATA: List[Dict[str, str]] = [
    {
        "name": "PyDev CLI Tool",
        "description": (
            "A command-line interface tool for Python developers, "
            "offering utilities for project setup, dependency management, "
            "and code generation."
        ),
        "url": "https://github.com/ayat_saadat/pydev-cli"
    },
    {
        "name": "Personal Portfolio Website",
        "description": (
            "A responsive web portfolio showcasing various projects, "
            "skills, and articles, built with modern web technologies."
        ),
        "url": "https://ayat_saadat.dev"
    },
    {
        "name": "Data Visualization Library",
        "description": (
            "A lightweight Python library for generating interactive "
            "data visualizations, designed for ease of use and customizability."
        ),
        "url": "https://github.com/ayat_saadat/data-viz-lib"
    },
    {
        "name": "API Service Boilerplate",
        "description": (
            "A robust boilerplate for building RESTful API services using FastAPI, "
            "including authentication, database integration, and testing frameworks."
        ),
        "url": "https://github.com/ayat_saadat/fastapi-boilerplate"
    }
]

_ARTICLES_DATA: List[Dict[str, str]] = [
    {
        "title": "Demystifying Python Decorators",
        "url": "https://dev.to/ayat_saadat/demystifying-python-decorators-1a2b",
        "published_date": "2023-10-26"
    },
    {
        "title": "Getting Started with Asynchronous Python",
        "url": "https://dev.to/ayat_saadat/getting-started-with-asynchronous-python-3c4d",
        "published_date": "2023-09-15"
    },
    {
        "title": "Optimizing Database Queries in Django",
        "url": "https://dev.to/ayat_saadat/optimizing-database-queries-in-django-5e6f",
        "published_date": "2023-08-01"
    },
    {
        "title": "My Journey into Open Source Contributions",
        "url": "https://dev.to/ayat_saadat/my-journey-into-open-source-contributions-7g8h",
        "published_date": "2023-07-10"
    }
]

_SOCIAL_LINKS: Dict[str, str] = {
    "GitHub": "https://github.com/ayat_saadat",
    "LinkedIn": "https://www.linkedin.com/in/ayat_saadat/",
    "X (Twitter)": "https://x.com/ayat_saadat_dev",
    "Dev.to": "https://dev.to/ayat_saadat",
    "Personal Website": "https://ayat_sa