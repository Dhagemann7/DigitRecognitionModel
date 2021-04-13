import struct
import numpy
import os
import tkinter
from tkinter import *

#https://www.codespeedy.com/convert-rgb-to-hex-color-code-in-python/
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

#https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
dir_path = os.path.dirname(os.path.realpath(__file__))
lib_path = dir_path[:-4] + 'lib'
#https://medium.com/the-owl/converting-mnist-data-in-idx-format-to-python-numpy-array-5cb9126f99f1
filename = {'images' : (lib_path + '\\train-images.idx3-ubyte'), 'labels' : (lib_path + '\\train-labels.idx1-ubyte')}
trainImagesFile = open(filename['images'],'rb')
trainImagesFile.seek(0)
magic = struct.unpack('>4B',trainImagesFile.read(4))

Img = struct.unpack('>I',trainImagesFile.read(4))[0] #num of images
nR = struct.unpack('>I',trainImagesFile.read(4))[0] #num of rows
nC = struct.unpack('>I',trainImagesFile.read(4))[0] #num of columns

images_array = numpy.zeros((Img,nR,nC))

nBytesTotal = Img*nR*nC*1 #since each pixel data is 1 byte
images_array = numpy.asarray(struct.unpack('>'+'B'*nBytesTotal,trainImagesFile.read(nBytesTotal))).reshape((Img,nR,nC))
frames = []
first = True
top = tkinter.Tk()
if(first):
    for x in range(len(images_array[0])):
        for y in range(len(images_array[0][0])):
            tkinter.Label(top, bg =  '#'+rgb_to_hex((images_array[0][x][y], images_array[0][x][y], images_array[0][x][y])),
            bd = 0, padx = 0, pady = 0, width = 1 px, height = 1 px, borderwidth=0 ).grid(row=x,column=y)
first = False
top.mainloop()
