#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
# 
# Convert ogv file to mpg
# 
# Copyright (C) 2009 Lorenzo Carbonell
# lorenzo.carbonell.cerezo@gmail.com
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# 
# 
import os, subprocess
from sys import argv
from string import join
def normaliza(cadena):
    cadena=cadena.replace(' ','_')
    cadena=cadena.replace('.','_')
    return cadena
def restaura(cadena):
    cadena=cadena.replace('_',' ')
    return cadena
def codifica(file):
    respuesta=False
    outfd = open('archivo_out', 'w+')
    errfd = open('archivo_err', 'w+')
    comando="ffmpeg -i "+"'"+file+"' -r 24 salida.mpg"
    retcode=subprocess.call(comando,shell=True, stdout=outfd, stderr=errfd)
    outfd.close()
    errfd.close()
    fd = open('archivo_out', 'r')
    output = fd.read()
    fd.close()
    fd = open('archivo_err', 'r')
    err = fd.read()
    fd.close()
    print 'stdout: %s\n' % output
    print 'stderr: %s' % err
    os.remove('archivo_out')
    os.remove('archivo_err')
    return retcode
#-----------------------------------------------------------------------------------------------------------------------    
if len(argv) < 2:
  print 'At least one ogv file to convert'
  sys.exit()


files=argv[1:]
for file in files:
  file1=join(file.split('.')[:-1],'.')
  entrada="or_"+normaliza(file1)+".ogv"
  salida=restaura(file1)+".mpg"
  print'---------------------------------------------------------------------\n'
  print "Renombrando "+file+" a "+entrada+"\n"
  os.rename(file,entrada)
  print "Codificando "+entrada+" a salida.mpg\n"
  if codifica(entrada)==0:
      print "Renombrando salida.mpg a "+salida+"\n"
      os.rename("salida.mpg",salida)
      print "Borrando "+entrada+"\n"
      os.remove(entrada)#depende de si funciona
  print'---------------------------------------------------------------------\n'
