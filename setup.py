# -*- coding: UTF-8 -*-
"""
Setup module for Pylint plugin for Firefly.
"""
from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as readme, open(
    "CHANGELOG.md", encoding="utf-8"
) as changelog:
    LONG_DESCRIPTION = readme.read() + "\n" + changelog.read()

setup(
    name="firefly-pylint",
    url="https://github.com/fireflyhealth/firefly-pylint/",
    author="FireflyHealth",
    description="Pylint plugin for Firefly stack",
    long_description=LONG_DESCRIPTION,
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pylint-plugin-utils>=0.7",
        "pylint>=2.13.9,<3",
    ],
    extras_require={
        "for_tests": [
            "astroid==2.11.5",
            "pytest==6.1.1",
            "Django==3.2.14",
            "pylint==2.13.9",
        ],
    },
    license="GPLv2",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Topic :: Software Development :: Quality Assurance",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Framework :: Django :: 3.2",
    ],
    keywords=["pylint", "plugin"],
    zip_safe=False,
    project_urls={
        "Changelog": "https://github.com/fireflyhealth/firefly-pylint/blob/master/CHANGELOG.md",
    },
)
