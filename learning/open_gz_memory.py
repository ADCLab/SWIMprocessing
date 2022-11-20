#! /usr/bin/env python2
from io import StringIO 
import gzip


fname='nas_enroute_1668149581.njson.gz'
compressedFile = StringIO.StringIO(fname)
decompressedFile = gzip.GzipFile(fileobj=compressedFile)
a=decompressedFile.read()