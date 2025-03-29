"""
=====================CAUTION=======================
DO NOT DELETE THIS FILE SINCE IT IS PART OF NROBO
FRAMEWORK AND IT MAY CHANGE IN THE FUTURE UPGRADES
OF NROBO FRAMEWORK. THUS, TO BE ABLE TO SAFELY UPGRADE
TO LATEST NROBO VERSION, PLEASE DO NOT DELETE THIS
FILE OR ALTER ITS LOCATION OR ALTER ITS CONTENT!!!
===================================================

This module has actions pertaining to nRoBo compiling.
This is yet an experimental stage.

@author: Panchdev Singh Chauhan
@email: erpanchdev@gmail.com
"""

import os

current_dir = os.getcwd()

import compileall

print(f"Compiling source code at path: {current_dir}{os.sep}nrobo{os.sep}")
compileall.compile_dir(f"{current_dir}{os.sep}nrobo{os.sep}", force=True, quiet=1)
compileall.compile_file(f"{current_dir}{os.sep}nrobo{os.sep}conftest.py")
