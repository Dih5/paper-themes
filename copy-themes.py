#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import matplotlib

import shutil
import os
import glob

stylelib_path=os.path.join(matplotlib.get_configdir(), "stylelib")
file_list=glob.glob('*.mplstyle')

try:
    if not os.path.exists(stylelib_path):
        os.makedirs(stylelib_path)
    for f in file_list:
        shutil.copy2(f,os.path.join(stylelib_path,f))
    print("Themes copied to %s" % stylelib_path)
except:
    print("An error occured! Try to manually copy the *.mplstyle files. E.g.:\nmkdir -p %s && cp *.mplstyle %s" % (stylelib_path,stylelib_path) )
