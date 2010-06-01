#!/usr/bin/python
# Convert pnf to pdf
# by invoking Image
# Lorenzo Carbonell <lorenzo.carbonell.cerezo@gmail.com>

from os import execvp
from sys import argv
from os import path
import Image

if len(argv) < 1:
	print 'At least two files to rotate'
	sys.exit()

files=argv[1:]
for file in files:
	im=Image.open(file)
	tf=path.splitext(file)
	salida=tf[0]+'.pdf'
	im.save(salida)
	print 'File created: '+salida
