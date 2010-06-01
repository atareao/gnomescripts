#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
# 
# Convert svg files to png files using inkscape
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
"""Usage: svg2png.py file [files...]

Convert svg files to png\
"""

import os, sys

if len(sys.argv) <= 1:
  raise SystemExit(__doc__)

for input in sys.argv[1:]:
  if not input.endswith('.svg'):
      print 'skipping "%s": it is not an svg file' % input
      continue

  output = input.replace('.svg', '.png')
  # Convert using inkscape
  if os.system('inkscape --export-png="%s"  --file="%s"' % (output, input)) != 0:
    print 'inkscape png conversion fails'
    sys.exit(1)

