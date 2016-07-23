#!C:\Python27\python.exe

import os
import re

from pyth.plugins.rtf15.reader import Rtf15Reader
from pyth.plugins.xhtml.writer import XHTMLWriter
from dehtml import dehtml

root = '.'

input = raw_input(
    "Input the word you want to search, followed by a comma and then its weight, then hit enter. ex; fish, 3. Enter ; when finished.\n")

words = ()

while input != ';':
    i_list = input.split(', ')
    words += ([i_list[0], i_list[1]],)
    input = raw_input("Another word? ; to quit\n")

scores = {w: float(n) for w, n in words}
total = 0

output = open("results.txt", "w")

results = {}

for dirs, subdirs, files in os.walk(root):
    for f in files:
        if f.endswith('.rtf'):
            doc = Rtf15Reader.read(open(f, "rb"))
            total = 0
            text = dehtml(XHTMLWriter.write(doc).read().lower().split())
            for word in text:
                word = re.sub('\W+', '', word)
                total += scores.get(word, 0)

            results[f] = total

for key, value in sorted(results.items()):
    output.write(key + "       " + str(value) + "\n")

print "Finished! Check results.txt"
raw_input("\nPress enter to close.")
