#!/usr/bin/python3
import codecs
import struct
infile = open('dualimageheaderascii', 'r')
outfile = open('dualimageheader.bin', 'wb')
for line in infile:
    string = codecs.decode(line[:-1], "hex")
    outfile.write(string)
