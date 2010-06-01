#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
# 
# Convert pdf files to svg files
# 
# Copyright (C) 2010 Lorenzo Carbonell
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
"""Usage: pdf2svg.py file [files...]

Convert pdf files to svg\
"""

import os, sys

if len(sys.argv) <= 1:
  raise SystemExit(__doc__)

for input in sys.argv[1:]:
  if not input.endswith('.pdf'):
      print 'skipping "%s": it is not an pdf file' % input
      continue

  output = input.replace('.pdf', '.svg')
  # Convert using inkscape
  if os.system('pdf2svg "%s" "%s"' % (input, output)) != 0:
    print 'pdf conversion fails'
    sys.exit(1)

