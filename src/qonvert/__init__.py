# encoding: utf-8
import os

__author__ = 'Roberto <rsanchez@qualityobjects.com>'


with open(os.path.join(os.path.dirname(__file__), 'version.txt')) as ver: 
    __version__ = ver.read().strip()

