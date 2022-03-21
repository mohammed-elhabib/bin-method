import time

import numpy as np
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
    printImage(imag_host, "imag_host.png")
    watermark_size = 64
    imag_w = readWaterImage(image_water_mark, watermark_size)

    print("read", height, width)
    block = imag_host[np.int(height / 2) - watermark_size:np.int(height / 2) + np.int(watermark_size),
            np.int(width / 2) - watermark_size:np.int(width / 2) + np.int(watermark_size)]
    print("block", len(block))
    block_bin = binary_repr_v(block, 8)
    print("block_bin", len(block_bin))

    image_w_4 = np.zeros((watermark_size * 2, watermark_size * 2))
    image_w_4[:watermark_size, :watermark_size] = np.copy(imag_w)
    image_w_4[:watermark_size, watermark_size:] = np.rot90(np.copy(imag_w), 3)
    image_w_4[watermark_size:, :watermark_size] = np.rot90(np.copy(imag_w), 1)
    image_w_4[watermark_size:, watermark_size:] = np.rot90(np.copy(imag_w), 2)
    image_w_bin_4=binary_repr_v(np.int32(image_w_4), 8).ravel()
    print(len(image_w_bin_4))
    print("1")
    i_w = 0
    for x in range( len(block_bin)):
        for y in range( len(block_bin[0])):
            if i_w < len(image_w_bin_4):
                print(i_w)
                block_bin[x][y][0] = int(str(block_bin[x][y][0][:6]) + str(image_w_bin_4[i_w])[:2])
                block_bin[x][y][1] = int(str(block_bin[x][y][1])[:5] + str(image_w_bin_4[i_w])[2:5])
                print(str(image_w_bin_4[i_w]))
                block_bin[x][y][2] = int(str(block_bin[x][y][2])[:5] + str(image_w_bin_4[i_w])[5:8])
            else:
                print(i_w)
            i_w += 1
    block_after_edit = np.array([int(bin, 2) for bin in block_bin.ravel()]).reshape(
        (watermark_size * 2, watermark_size * 2, 3))
    imag_host[np.int(height / 2) - watermark_size:np.int(height / 2) + np.int(watermark_size),
    np.int(width / 2) - watermark_size:np.int(width / 2) + watermark_size] = block_after_edit
    printImage(imag_host, image_water_marked)
    # imag_host_rotate_1
    print("fin")


def extract_watermark(image_water_marked, image_water_mark_extract):
    binary_repr_v = np.vectorize(np.binary_repr)
    watermark_size = 64
    height, width, imag_host_w = readImage2(image_water_marked)
    block_w = imag_host_w[np.int(height / 2) - watermark_size:np.int(height / 2) + np.int(watermark_size),
              np.int(width / 2) - watermark_size:np.int(width / 2) + np.int(watermark_size)]
    block_bin_w = binary_repr_v(block_w, 8)
    imag_w_bin_w_all = np.zeros(watermark_size * watermark_size*4)
    print("1")
    i_w = 0
    for x in range(0, len(block_bin_w)):
        for y in range(0, len(block_bin_w)):
            if i_w <= len(imag_w_bin_w_all):
                imag_w_bin_w_s = block_bin_w[x][y][0][-2:] + block_bin_w[x][y][1][-3:] + block_bin_w[x][y][2][-3:]
                imag_w_bin_w_all[i_w] = int(imag_w_bin_w_s, 2)
            i_w += 1
    imag_w_bin_w_all = imag_w_bin_w_all.reshape((watermark_size * 2, watermark_size * 2))
    watermark1=imag_w_bin_w_all[:watermark_size, :watermark_size]
    watermark2=np.rot90(imag_w_bin_w_all[:watermark_size, watermark_size:])
    watermark3=np.rot90(imag_w_bin_w_all[watermark_size:, :watermark_size],3)
    watermark4=np.rot90(imag_w_bin_w_all[watermark_size:, watermark_size:],2)
    printImage(watermark1, image_water_mark_extract+"_1.png")
    printImage(watermark2, image_water_mark_extract+"_2.png")
    printImage(watermark3, image_water_mark_extract+"_3.png")
    printImage(watermark4, image_water_mark_extract+"_4.png")
