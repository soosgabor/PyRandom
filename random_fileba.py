import time
import sys 
import subprocess
import os

if len(sys.argv) != 3:
    print('usage: file_finder.py [search wildcard] [target dir]')
    sys.exit(1)

for name in os.listdir("apa"):
    if name.endswith(".txt"):
        print(name)

a = [name for name in os.listdir("apa") if name.endswith(".txt")]
print(a)

curpath=os.path.abspath('.')
print(curpath)

def make_dir(path='backup'):
    if not os.path.exists(path):
        os.makedirs(path)
    