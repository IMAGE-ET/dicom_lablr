#!/usr/bin/env python

# import libraries
import os

# define parts of program call
base_call = 'main.py'
path_call = '-p data/ex2'

# make into a list
cmd_lst = [
    base_call,
    path_call,
]

# source and run file
os.system(" ".join(cmd_lst))
