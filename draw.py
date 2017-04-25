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
#    coords = sorted(coords,key=lambda x: x[0])
    coords = sorted(coords,key=operator.itemgetter(0))

    print coords


#im = Image.open( outfile )

read_file()
