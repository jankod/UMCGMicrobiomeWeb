import platform

import os

print("python version ", platform.python_version())

if os.getenv('VIRTUAL_ENV'):
    print('Using Virtualenv')
else:
    print('Not using Virtualenv')

import sys

print(sys.executable)
