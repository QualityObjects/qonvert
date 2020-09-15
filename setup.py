#!/usr/bin/env python3
# encoding: utf-8
"""
Created on 2020-02-08

@author: rsanchez@qualityobjects.com
"""
from distutils.core import setup
from setuptools import find_packages

import os, shutil, sys
from os.path import expanduser

MAIN_MODULE = "qonvert"
user_home = expanduser("~")

if "bdist" in sys.argv:
    print("bdist option is not supported, use bdist_wheel instead")
    sys.exit(-1)

is_binary_build = set(["bdist", "bdist_wheel"]) & set(sys.argv)

def create_build_info():
    try:
        os.system(
            "git log -1 --date=iso | head -4 > %s"
            % (os.path.join("src", MAIN_MODULE, "build.txt"))
        )
    except:
        pass  # Probably in Windows


package_dir = {MAIN_MODULE: os.path.join("src", MAIN_MODULE)}

script_files = ["qonvert-server"]

dist_object = setup(
    name="qonvert-server",
    version=open(os.path.join("src", MAIN_MODULE, "version.txt")).read(),
    author=u"Quality Objects S.L.",
    author_email="rsanchez@qualityobjects.com",
    packages=find_packages("src"),
    include_package_data=True,
    scripts=list(map(os.path.join, ["script"] * len(script_files), script_files)),
    url="https://www.qodev.es/qonvert",
    license=open("LICENSE").read(),
    description="QOnvert server",
    long_description=open("README.md").read(),
    data_files=[],
    package_dir=package_dir,
    setup_requires=[],
    install_requires='pillow>=7 fastapi>=0.61 python-multipart'.split(' '),    
    classifiers=[
        "Environment :: Web",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: MIT",
        "Topic :: QOnvert :: Server",
        "Topic :: QOnvert :: Web",
        "Topic :: QOnvert :: REST API",
    ],
)


if set(["sdist", "bdist", "bdist_wheel"]) & set(sys.argv):
    _, _, fileout = dist_object.dist_files[0]
    print("\nDistribution file generated at: \n\t%s" % fileout)
# http://the-hitchhikers-guide-to-packaging.readthedocs.org/en/latest/creation.html
