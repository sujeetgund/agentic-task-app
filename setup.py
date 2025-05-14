from setuptools import setup, find_packages
from pathlib import Path

def get_requirements(filepath: str) -> list[str]:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        return []


setup(
    name="agentic-task-app",
    version="0.1.0",
    author="Sujeet Gund",
    author_email="sujeetgund@gmail.com",
    description="Agentic AI app built with Agno to extract, store, and manage user tasks — with optional Google Calendar integration and modular DB backend.",
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/sujeetgund/agentic-task-app",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=get_requirements("requirements.txt"),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
