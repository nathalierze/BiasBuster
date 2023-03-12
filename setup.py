import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "bias-metrics",
    version = "0.0.1",
    author = "Nathalie Rzepka",
    # author_email = "author@example.com",
    description = "A Python package to check for algorithmic bias.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/nathalierze/bias-metrics",
    project_urls = {
        "Bug Tracker": "https://github.com/nathalierze/bias-metrics/issuesL",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)