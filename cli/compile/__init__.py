import os
import sys

current_dir = os.getcwd()
print(f"ExecutionDir: {current_dir}")
print(f"System recursion limit: {sys.getrecursionlimit()}")

import compileall

print(f"Compiling source code at path: {current_dir}{os.sep}nrobo{os.sep}")
compileall.compile_dir(f"{current_dir}{os.sep}nrobo{os.sep}", force=True, quiet=1)
print(os.path.exists(f"{current_dir}{os.sep}nrobo{os.sep}__init__.pyc"))
print(os.path.exists(f"{current_dir}{os.sep}nrobo{os.sep}__init__.pyo"))

compileall.compile_file(f"{current_dir}{os.sep}nrobo{os.sep}conftest.py")
