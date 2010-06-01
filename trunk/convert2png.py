#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
# 
# Convert image to png by invoking PIL
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
from PIL import Image

if len(argv) < 2:
  print 'At least one image to convert'
  sys.exit()


files=argv[1:]
for file in files:
  im=Image.open(file)
  tf=path.splitext(file) 
  salida=tf[0]+'.png'
  im.save(salida)


