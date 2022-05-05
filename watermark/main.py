import math
from math import log10, sqrt

import cv2
import numpy as np
from PIL import Image

from attack2 import noisy
from bin_method import embedd_watermark, extract_watermark, printImage, readImage, readWaterImage


def cut(param, image_water_marked):
    height = 1200
    width = 1200
    img = Image.open(image_water_marked).resize((height, width), 1)
    image = np.array(img.getdata()).reshape((width, height, 3))
    if 1 in param:
        for row in range(int(height / 2)):
            for coll in range(int(width / 2)):
                image[row][coll] = 0
    if 4 in param:
        for row in range(int(height / 2), height):
            for coll in range(int(width / 2), width):
                image[row][coll] = 0
    if 3 in param:
        for row in range(int(height / 2), height):
            for coll in range(int(width / 2)):
                image[row][coll] = 0
    if 2 in param:
        for row in range(int(height / 2)):
            for coll in range(int(width / 2), width):
                image[row][coll] = 0
    return image


image_host = "input/X-Ray-7.jfif"
image_water_marked = "image_water_marked.png"
image_water_mark = "input/w.png"
image_water_mark_extract = "mark_extract"
# attacks  gauss speckle s&p poisson
attack_gauss_image = "attacks/attack_gauss_image.png"
attack_speckle_image = "attacks/attack_speckle_image.png"
attack_s_p_image = "attacks/attack_s_p_image.png"
attack_poisson_image = "attacks/attack_poisson_image.png"
attack_croppe_image = "attacks/attack_croppe_image.png"
attack_gauss_image_w = "attacks/attack_gauss_image_w.png"
attack_speckle_image_w = "attacks/attack_speckle_image_w.png"
attack_s_p_image_w = "attacks/attack_s_p_image_w.png"
attack_poisson_image_w = "attacks/attack_poisson_image_w.png"
attack_croppe_image_w = "attacks/attack_croppe_image_w.png"
embedd_watermark(image_host, image_water_mark, image_water_marked)
extract_watermark(image_water_marked, image_water_mark_extract)
# printImage(readWaterImage(image_water_mark, 64), "w_l.png")
attack_cut_0_image = "attacks/attack_cut_0_image.png"
attack_cut_0_image_w = "attacks/attack_cut_0_image_w"

printImage(cut([2,3,1], image_water_marked), attack_cut_0_image)

printImage(noisy("gauss", image_water_marked), attack_gauss_image)
#printImage(noisy("speckle", image_water_marked), attack_speckle_image)
printImage(noisy("s&p", image_water_marked), attack_s_p_image)
# printImage(noisy("poisson", image_water_marked), attack_poisson_image)
printImage(noisy("croppe", image_water_marked), attack_croppe_image)


#extract_watermark(attack_speckle_image, attack_speckle_image_w)
# extract_watermark(attack_poisson_image, attack_poisson_image_w)
extract_watermark(attack_gauss_image, attack_gauss_image_w)
extract_watermark(attack_s_p_image, attack_s_p_image_w)
extract_watermark(attack_croppe_image, attack_croppe_image_w)
extract_watermark(attack_cut_0_image, attack_cut_0_image_w)


def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)

    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    PSNR = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
    return PSNR


original = cv2.imread("w_l.png")

print("attack_croppe_image_w")
compressed = cv2.imread("attacks/attack_croppe_image_w.png_1.png", 1)
value = PSNR(original, compressed)
print(f"PSNR 1 value is {value} dB")


compressed = cv2.imread("attacks/attack_croppe_image_w.png_2.png", 1)
value = PSNR(original,compressed)
print(f"PSNR 2 value is {value} dB")
compressed = cv2.imread("attacks/attack_croppe_image_w.png_3.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 3 value is {value} dB")
compressed = cv2.imread("attacks/attack_croppe_image_w.png_3.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 4 value is {value} dB")
print("image_water_mark_extract")
compressed = cv2.imread("attacks/attack_s_p_image_w.png_1.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 1 value is {value} dB")
compressed = cv2.imread("attacks/attack_s_p_image_w.png_2.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 2 value is {value} dB")
compressed = cv2.imread("attacks/attack_s_p_image_w.png_3.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 3 value is {value} dB")
compressed = cv2.imread("attacks/attack_s_p_image_w.png_4.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 4 value is {value} dB")
print("attack_gauss_image_w")
compressed = cv2.imread("attacks/attack_gauss_image_w.png_1.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 1 value is {value} dB")
compressed = cv2.imread("attacks/attack_gauss_image_w.png_2.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 2 value is {value} dB")
compressed = cv2.imread("attacks/attack_gauss_image_w.png_3.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 3 value is {value} dB")
compressed = cv2.imread("attacks/attack_gauss_image_w.png_4.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 4 value is {value} dB")

print("attack_s_p_image")
compressed = cv2.imread("attacks/attack_s_p_image_w.png_1.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 1 value is {value} dB")
compressed = cv2.imread("attacks/attack_s_p_image_w.png_2.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 2 value is {value} dB")
compressed = cv2.imread("attacks/attack_s_p_image_w.png_3.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 3 value is {value} dB")
compressed = cv2.imread("attacks/attack_s_p_image_w.png_4.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 4 value is {value} dB")


print("attack_gauss_image.png")
compressed = cv2.imread("attacks/attack_gauss_image_w.png_1.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 1 value is {value} dB")
compressed = cv2.imread("attacks/attack_gauss_image_w.png_2.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 2 value is {value} dB")
compressed = cv2.imread("attacks/attack_gauss_image_w.png_3.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 3 value is {value} dB")
compressed = cv2.imread("attacks/attack_gauss_image_w.png_4.png", 1)
value = PSNR(compressed, original)
print(f"PSNR 4 value is {value} dB")
#compressed = cv2.imread(attack_s_p_image_w, 1)
#value = PSNR(compressed,original)
#print(f"PSNR value is {value} dB")

print("attack_poisson_image_w")
#compressed = cv2.imread(attack_poisson_image_w, 1)
#value = PSNR(compressed,original )
#print(f"PSNR value is {value} dB")

#print("attack_speckle_image_w")
#compressed = cv2.imread(attack_speckle_image_w, 1)
#value = PSNR(compressed,original )
#print(f"PSNR value is {value} dB")

#print("attack_croppe_image_w")
#compressed = cv2.imread(attack_croppe_image_w, 1)
#value = PSNR(compressed,original )
#print(f"PSNR value is {value} dB")
#original = cv2.imread("imag_host.png")

#print("original")
#compressed = cv2.imread(image_water_marked, 1)

#value = PSNR(compressed,original )
#print(f"PSNR value is {value} dB")
