#!/usr/bin/python
# Rotate all pages in pdf files counter clockwise 90 degrees 
# by invoking pdftk
# Lorenzo Carbonell <lorenzo.carbonell.cerezo@gmail.com>

from os import execvp
from sys import argv
from os import path

if len(argv) < 1:
	print 'At least two files to rotate'
	sys.exit()

files=argv[1:]
for file in files:
	argumentos=[]
	argumentos.append('pdftk')
	argumentos.append(file)
	argumentos.append('cat')
	argumentos.append('1-endW')
	argumentos.append('output')
	tf=path.splitext(file) 
	salida=tf[0]+"_R90CC"+tf[1]
	argumentos.append(salida)
	print 'File created: '+salida
	execvp('pdftk',argumentos)
