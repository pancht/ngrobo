import os
import sys

current_dir = os.getcwd()

import compileall

print(f"Compiling source code at path: {current_dir}{os.sep}nrobo{os.sep}")
compileall.compile_dir(f"{current_dir}{os.sep}nrobo{os.sep}", force=True, quiet=1)
compileall.compile_file(f"{current_dir}{os.sep}nrobo{os.sep}conftest.py")
