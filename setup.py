import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requirements = []
with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="notion",
    version="0.0.26",
    author="Jamie Alexandre",
    author_email="jamalex+python@gmail.com",
    description="Unofficial Python API client for Notion.so",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jamalex/notion-py",
    install_requires=requirements,
    include_package_data=True,
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
