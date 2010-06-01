#!/usr/bin/python
# Rotate all pages in pdf files 90 clockwise degrees
# by invoking pdftk
# Lorenzo Carbonell <lorenzo.carbonell.cerezo@gmail.com>

from os import execvp
from sys import argv

if len(argv) < 1:
	print 'At least two files to rotate'
	sys.exit()

files=argv[1:]
for file in files:
	argumentos=[]
	argumentos.append('pdftk')
	argumentos.append(file)
	argumentos.append('cat')
	argumentos.append('1-endE')
	argumentos.append('output')
	tf=os.path.splitext(file) 
	print tf
	argumentos.append('out.pdf')
	print 'File created: out.pdf'
	execvp('pdftk',argumentos)
