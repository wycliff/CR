# -*- coding: utf-8 -*-
import sys
from cx_Freeze import setup, Executable

includes=[]

#Platform specific details
base = None #global variable declaration 
options = {'build_exe': {'include_files': ['resources/']}}

if sys.platform == 'win32':
    base = 'Win32GUI'


executables = [
    Executable('alpr.py', base=base)
]


setup(name='ALPR',
      version='0.0.1',
      description='ALPR',
      executables=executables,
	  options=options
      )

# Run in cmd using the command below 

#python setup.py build