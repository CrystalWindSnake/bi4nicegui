#!/usr/bin/env python
"""The setup script."""

from setuptools import setup, find_packages
import bi4nicegui


with open("README.md", encoding="utf8") as readme_file:
    readme = readme_file.read()

requirements = ["pandas", "ex4nicegui", "typing_extensions"]

test_requirements = ["pytest>=3"]

setup(
    author="carson_jia",
    author_email="568166495@qq.com",
    python_requires=">=3.7",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="...",
    entry_points={
        # 'console_scripts': [
        #     'test_prj=test_prj.cli:main',
        # ],
    },
    install_requires=requirements,
    license="MIT license",
    # long_description=readme,
    include_package_data=True,
    keywords=["nicegui",'pybi-next', "bi4nicegui", "webui"],
    name="bi4nicegui",
    packages=find_packages(include=["bi4nicegui", "bi4nicegui.*"]),
    data_files=[
    ],
    test_suite="__tests",
    tests_require=test_requirements,
    url="",
    version=bi4nicegui.__version__,
    zip_safe=False,
)
