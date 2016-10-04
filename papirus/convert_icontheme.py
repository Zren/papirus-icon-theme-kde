#!/usr/bin/python3

from convert_icon import convertIconSvg
import glob
import os

for filename in glob.iglob('**/*.svg', recursive=True):
	print(filename)
	if os.path.islink(filename):
		continue
	convertIconSvg(filename)


