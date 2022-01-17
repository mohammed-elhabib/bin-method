import time

import numpy as np
import pandas as pd
from PIL import Image


def readWaterImage(imageName, size):
    img = Image.open(imageName).resize((size, size), 1)
    # Convert RGB image to gray scale
    img = img.convert('L')
    imageArray = np.array(img.getdata(), dtype=np.int).reshape((size, size))
    return imageArray


def readImage(imageName, size):
    img = Image.open(imageName).resize((size, size), 1)
    height, width = img.size
    return height, width, np.array(img.getdata()).reshape((width, height, 3))
def readImage2(imageName):
    img = Image.open(imageName)
    height, width = img.size
    return height, width, np.array(img.getdata()).reshape((width, height, 3))


def printImage(imageArray, name):
    imageArrayCopy = imageArray.astype("uint8")
    img = Image.fromarray(imageArrayCopy)
    img.save(name)




def embedd_watermark(image_host, image_water_mark, image_water_marked):
    binary_repr_v = np.vectorize(np.binary_repr)

    height, width, imag_host = readImage(image_host, 1200)
    watermark_size = 64
    imag_w = readWaterImage(image_water_mark, watermark_size)
    # printImage(imag_w,"bin.png")
    print("read", height, width)
    block = imag_host[np.int(height / 2) - watermark_size * 4:np.int(height / 2) + np.int(watermark_size * 4),
            np.int(width / 2) - watermark_size * 4:np.int(width / 2) + np.int(watermark_size * 4)]
    print("block", len(block))
    block_bin = binary_repr_v(block, 8)
    print("block_bin", len(block_bin))
    imag_w_bin = binary_repr_v(imag_w, 8).ravel()
    print("1")
    i_w = 0
    for x in range(0, len(block_bin), 8):
        for y in range(0, len(block_bin), 8):
            if i_w <= len(imag_w_bin):

                block_bin[x][y][0] = int(str(block_bin[x][y][0][:5]) + str(imag_w_bin[i_w])[:2])
                block_bin[x][y][1] = int(str(block_bin[x][y][1])[:5] + str(imag_w_bin[i_w])[2:5])
                block_bin[x][y][2] = int(str(block_bin[x][y][2])[:5] + str(imag_w_bin[i_w])[5:8])
                if i_w < 10:
                    print(block_bin[x][y])
            i_w += 1
    block_after_edit = np.array([int(bin, 2) for bin in block_bin.ravel()]).reshape(
        (watermark_size * 8, watermark_size * 8, 3))
    block_after_edit = block_after_edit.reshape((watermark_size * 8, watermark_size * 8, 3))
    imag_host[np.int(height / 2) - watermark_size * 4:np.int(height / 2) + np.int(watermark_size * 4),
    np.int(width / 2) - watermark_size * 4:np.int(width / 2) + np.int(watermark_size * 4)] = block_after_edit
    printImage(imag_host, image_water_marked)
    # imag_host_rotate_1
    print("fin")


def extract_watermark(image_water_marked, image_water_mark_extract):
    binary_repr_v = np.vectorize(np.binary_repr)
    watermark_size = 64
    height, width, imag_host_w = readImage2(image_water_marked)

    block_w = imag_host_w[np.int(height / 2) - watermark_size * 4:np.int(height / 2) + np.int(watermark_size * 4),
              np.int(width / 2) - watermark_size * 4:np.int(width / 2) + np.int(watermark_size * 4)]
    block_bin_w = binary_repr_v(block_w, 8)
    imag_w_bin_w = np.zeros(watermark_size * watermark_size)
    print("1")
    i_w = 0
    for x in range(0, len(block_bin_w), 8):
        for y in range(0, len(block_bin_w), 8):
            if i_w <= len(imag_w_bin_w):
                imag_w_bin_w_s = ""
                imag_w_bin_w_s = block_bin_w[x][y][0][-2:] + block_bin_w[x][y][1][-3:] + block_bin_w[x][y][2][-3:]
                if i_w < 10:
                    print(block_bin_w[x][y])
                imag_w_bin_w[i_w] = int(imag_w_bin_w_s, 2)
            i_w += 1
    imag_w_bin_w = imag_w_bin_w.reshape((watermark_size, watermark_size))
    print(imag_w_bin_w)
    printImage(imag_w_bin_w, image_water_mark_extract)



