import os
import time

def latest(num=1, path="."):
    """Returns the latest file(s) in a given directory"""
    os.chdir(path)
    dirfiles = os.listdir()
    sorted_files = sorted(dirfiles, key=lambda filestr: os.path.getmtime(filestr), reverse=True)
    results = []
    for i in range(0, num):
        results.append(sorted_files[i])
    return results
