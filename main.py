import os

import PyPDF2

root = os.path.dirname(os.path.dirname(__file__))

for subdir, dirs, files in os.walk(root):
    for file in files:
        path = subdir + os.sep + file

        if path.endswith(".py"):
            print(path)
