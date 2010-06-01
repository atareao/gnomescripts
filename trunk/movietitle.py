#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

#
# Correct name of the movie in a directory
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

import sys
import os
from sys import argv
from os import path

if len(argv) < 2:
  print 'At least one movie to correct'
  sys.exit()


files=argv[1:]
for file in files:
  (name,ext)=path.splitext(file)
  if (ext=='.avi') | (ext=='.mkv') | (ext=='.mpg'):
    name=name.lower()
    ext=ext.lower()
    name=name.replace('spanish','')
    name=name.replace('xvid','')
    name=name.replace('mp3','')
    name=name.replace('dvdrip','')
    name=name.replace('hdrip','')
    name=name.replace('by','')
    name=name.replace('freak','')
    name=name.replace('team','')
    name=name.replace('[','')
    name=name.replace('hd','')
    name=name.replace('dvd','')
    name=name.replace(']','')
    name=name.replace('1080','')
    name=name.replace('x264','')
    name=name.replace('english','')
    name=name.replace('ac3','')
    name=name.replace('emuleteca','')
    name=name.replace('hdgroup','')
    name=name.replace('group','')
    name=name.replace('bdrip','')
    name=name.replace('dxva','')
    name=name.replace('centraldivx','')
    name=name.replace('screener','')
    name=name.replace('-','')
    name=name.replace('subs','')
    #
    name=name.replace('720','')
    name=name.replace('rip','')
    name=name.replace('2000','')
    name=name.replace('2001','')
    name=name.replace('2002','')
    name=name.replace('2003','')
    name=name.replace('2004','')
    name=name.replace('2005','')
    name=name.replace('2006','')
    name=name.replace('2007','')
    name=name.replace('2008','')
    name=name.replace('2009','')
    name=name.replace('2010','')
    #
    name=name.replace('.',' ')
    name=name.rstrip()
    name=name.lstrip()
    name=name.capitalize()
    name=name.replace('( )','')
    name=name.replace('()','')
    name=name.rstrip()
    name=name.lstrip()
    hasta=name.find('  ')
    if(hasta>0):
      newfile=name[0:hasta]+ext
    else:
      newfile=name+ext
    print '-----------------------------------------------------------------------------------------------'
    print file
    print newfile
    os.rename(file,newfile)
