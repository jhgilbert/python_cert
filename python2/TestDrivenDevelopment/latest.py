import os
import time

def latest(path):
    """Returns the latest file(s) in a given directory"""
    os.chdir(path)
    dirfiles = os.listdir()
    sorted_files = sorted(dirfiles, key=lambda filestr: os.path.getmtime(filestr), reverse=True)
    return sorted_files[0:-2]
