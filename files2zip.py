#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
# 
# Zip all files in one zip
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
from sys import argv
from os import path
import zipfile

if len(argv) < 2:
  print 'At least one file to zip'
  sys.exit()


files=argv[1:]
salida='comprimido.zip'
zfile=zipfile.ZipFile(salida,'w')
for file in files:
  zfile.write(file,path.basename(file),zipfile.ZIP_DEFLATED)
zfile.close()


