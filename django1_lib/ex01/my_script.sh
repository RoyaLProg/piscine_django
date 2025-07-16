#!/bin/sh

pip --version

pip install -t local_lib -I --log install.log git+https://github.com/jaraco/path && python my_program.py
