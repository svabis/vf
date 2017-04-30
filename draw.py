#!/usr/bin/python
import os
import operator

from PIL import Image, ImageDraw


def read_file():
    coords = []

    infile = '/home/svabis/stat'
    lines = [line.rstrip('\n') for line in open(infile)]


    iter = 0
    for line in lines:
        l = line.split(" | ")

        if l[0] != iter:
            temp = [ iter,0 ]
            coords.append( temp )
#            print temp

        temp = [ l[0],l[1] ]
        coords.append( temp )
        iter += 1

#    coords = sorted(coords)
#    coords = sorted(coords,key=int x: x[0])
#    coords = sorted(coords,key=lambda x: x[0])
#    coords = sorted(coords,key=operator.itemgetter(0))

    c = []
    for n in range( 0, 142):
        for m in range( 0, 142):
            if coords[m][0] < coords[n][0]:
                print min(enumerate(coords))
                pos = min(enumerate(coords))[0]
                temp = coords[pos]
                c.append(  temp )
                coords.pop( pos )

    print coords
    print c

#    for n in range( 0, 142):
#        test = coords[n][0]
#        for m in range( 1, 142):
#            if coords[m][0] < coords[n][0]:
#                 print 'x'
#                 temp = coords[n]
#                 coords[n] = coords[m]
#                 coords[m] = temp
#    for c in coords:
#        print c[0]

#im = Image.open( outfile )

read_file()
