#!/usr/bin/env python
# Create reflexion
# by invoking PIL
# (c) 2009 Lorenzo Carbonell <lorenzo.carbonell.cerezo@gmail.com>, released under the terms of the GNU GPL v3.

from PIL import Image
from sys import argv
from os import path
import os
import math

# logarithmic shade
def sombrea(numero):
  res=255  
  if numero > 0:
    res = 255-math.log(numero)/math.log(255)*255
  return res

files=argv[1:]
for file in files:
  tf=path.splitext(file)
  fsalida=tf[0]+'_output.png'
  print fsalida
  im = Image.open(file)
  # test if image has transparency
  if im.mode != 'RGBA':
	  im = im.convert('RGBA')
  # flip the image
  im2 = im.transpose(Image.FLIP_TOP_BOTTOM)
  # creating gradient
  gradient = Image.new('L', (1,255))
  for y in range(255):
	  gradient.putpixel((0,y),sombrea(y))
  # resize the gradient to image
  alpha = gradient.resize(im2.size)
  # put alpha in the alpha band of im...'
  im2.putalpha(alpha)
  # write output file
  size = [im2.size[0],2*im2.size[1]]
  salida=im.copy()
  salida=salida.resize(size)
  # put top the original image
  salida.paste(im,[0,0,im.size[0],im.size[1]])
  # put botton the shadding image
  salida.paste(im2,[0,im.size[1],im.size[0],2*im2.size[1]])
  # write the result
  salida.save(fsalida)
