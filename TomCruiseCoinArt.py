#!/usr/bin/python

from collections import namedtuple
from math import sqrt
import random
import os
import sys
import time
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import PIL
import csv
import colorsys
import glob
import math
import json
import numpy
import numpy as np

from PIL import Image


print "Starting Tom Cruise Coin Portrait Now...."

Pic=sys.argv[1]
Width=sys.argv[2]
Height=sys.argv[3]
Coin=sys.argv[4]

def get_points(percent,coin):
    if coin=="Penny":
        im = Image.open('CleanPenny.png')
    if coin=="Nickel":
        im = Image.open('CleanNickel.png')
    im = im.resize((25,25), PIL.Image.ANTIALIAS)
    pixelMap = im.load()

    img = Image.new( im.mode, im.size)
    pixelsNew = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):

            if pixelMap[i,j][3]==0:
                pixelMap[i,j] = (255,255,255,255)
            else:
                pixelMap[i,j]=(int(pixelMap[i,j][0]*percent),int(pixelMap[i,j][1]*percent),int(pixelMap[i,j][2]*percent),int(pixelMap[i,j][3]))
            pixelsNew[i,j]=pixelMap[i,j]

    return img



new_im = Image.new('RGB', (300, 300))


for i in range(0,3):
    for j in range(0,3):
        im = get_points(0.4+i*0.3,Coin)
        new_im.paste(im, (i*100,j*100))
  


#new_im.show()

ODW=int(float(Width)/float(0.75))
ODH=int(float(Height)/float(0.75))

OD=32

print ODW
filename=Pic
pix = Image.open(filename)
pix = pix.resize((ODW,ODH), PIL.Image.ANTIALIAS)
gry = pix.convert('L')
pixelsStart = list(gry.getdata())


SwitchControl=[]

LightCount=0
TotalIt=[]
pp=[]
out = Image.new('RGB', (ODW*25, ODH*25))
for i in range(0,ODH):
    temp=[]
    print "Generating Row "+str(i)
    last="D"
    for j in range(0,ODW):
        
        val=i*ODW+j
        dark=0.5
        t="y"+str(i+1)+" x"+str(j+1)+" D"
        tt="D"
        if pixelsStart[val]>150:
            dark=1.0
            t="y"+str(i+1)+" x"+str(j+1)+" L"
            tt="L"
            LightCount=LightCount+1
        temp.append(tt)
        if last!=tt:
            SwitchControl.append("\n")
            SwitchControl.append(t)
            last=tt


        pp.append(t)
    
 
        im = get_points(dark,Coin)
        out.paste(im, (j*25,i*25))
    pp.append(" ")
    SwitchControl.append("\n")
    TotalIt.append(temp)


print LightCount
print ODH*ODW
print ODH*ODW-LightCount
out.save('out.bmp')

out.show()


OutS = ''.join(SwitchControl)

text_file = open("SwitchInstructions.txt", "w")
text_file.write(OutS)
text_file.close()




