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
import sys, time, traceback

########################################################################3
# Simple  audio encoder 
def recodeAudio( fName, fOutput, type, bitrate= None ):
  # ------------------------------------

  import pymedia.audio.acodec as acodec
  import pymedia.muxer as muxer
  # Open demuxer

  dm= muxer.Demuxer( fName.split( '.' )[ -1 ].lower() )
  f= open( fName, 'rb' )
  s= f.read( 90000 )
  dec= enc= mx= None
  print 'Recoding %s into %s' % ( fName, fOutput )
  while len( s ):
    frames= dm.parse( s )
    if frames:
      for fr in frames:
        # Assume for now only audio streams

        if dec== None:
          # Open decoder

          dec= acodec.Decoder( dm.streams[ fr[ 0 ] ] )
          print 'Decoder params:', dm.streams[ fr[ 0 ] ]
        
        # Decode audio frame

        r= dec.decode( fr[ 1 ] )
        if r:
          if bitrate== None:
            bitrate= r.bitrate
          
          # Open muxer and encoder

          if enc== None:
            params= { 'id': acodec.getCodecID(type),
                      'bitrate': bitrate,
                      'sample_rate': r.sample_rate,
                      'channels': r.channels }
            print 'Encoder params:', params
            mx= muxer.Muxer( type )
            stId= mx.addStream( muxer.CODEC_TYPE_AUDIO, params )
            enc= acodec.Encoder( params )
            fw= open(fOutput, 'wb')
            ss= mx.start()
            fw.write(ss)
        
          enc_frames= enc.encode( r.data )
          if enc_frames:
            for efr in enc_frames:
              ss= mx.write( stId, efr )
              if ss:
                fw.write(ss)
    
    s= f.read( 100000 )
  
  f.close()
  
  if fw:
    if mx:
      ss= mx.end()
      if ss:
        fw.write(ss)
    fw.close()

if len(argv) < 2:
  print 'At least one file to convert'
  sys.exit()

files=argv[1:]
for file in files:
  tf=path.splitext(file) 
  salida=tf[0]+'.mp3'
  recodeAudio( file,salida,'mp3')
  dumpWAV(file)


