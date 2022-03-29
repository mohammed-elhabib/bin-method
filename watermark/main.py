import math
from math import log10, sqrt

import cv2
import numpy as np
from PIL import Image

from attack2 import noisy
from bin_method import embedd_watermark, extract_watermark, printImage, readImage, readWaterImage

image_host = "input/X-Ray-7.jfif"
image_water_marked = "imag_host_1.png"
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
attack_croppe_image_w ="attacks/attack_croppe_image_w.png"
embedd_watermark(image_host, image_water_mark, image_water_marked)
extract_watermark(image_water_marked, image_water_mark_extract)
printImage(readWaterImage(image_water_mark,64),"w_l.png")

printImage(noisy("gauss", image_water_marked), attack_gauss_image)
printImage(noisy("speckle", image_water_marked), attack_speckle_image)
printImage(noisy("s&p", image_water_marked), attack_s_p_image)
printImage(noisy("poisson", image_water_marked), attack_poisson_image)
printImage(noisy("croppe", image_water_marked),attack_croppe_image)
extract_watermark(attack_speckle_image, attack_speckle_image_w)
extract_watermark(attack_poisson_image, attack_poisson_image_w)
extract_watermark(attack_gauss_image, attack_gauss_image_w)
extract_watermark(attack_s_p_image, attack_s_p_image_w)
extract_watermark(attack_croppe_image, attack_croppe_image_w)

def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if mse == 0:
        return 100
    PIXEL_MAX = 255.0
    PSNR = 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
    return PSNR

original = cv2.imread("w_l.png")

print("attack_gauss_image_w")
compressed = cv2.imread("attacks/attack_croppe_image_w.png_1.png", 1)
value = cv2.PSNR(original,compressed,255 )
print(f"PSNR 1 value is {value} dB")

compressed = cv2.imread("attacks/attack_croppe_image_w.png_2.png", 1)
value = PSNR(compressed,original )
print(f"PSNR 2 value is {value} dB")
compressed = cv2.imread("attacks/attack_croppe_image_w.png_3.png", 1)
value = PSNR(compressed,original )
print(f"PSNR 3 value is {value} dB")
compressed = cv2.imread("attacks/attack_croppe_image_w.png_3.png", 1)
value = PSNR(compressed,original )
print(f"PSNR 4 value is {value} dB")
print("image_water_mark_extract")
compressed = cv2.imread("attacks/attack_s_p_image_w.png_1.png", 1)
value = PSNR(compressed,original )
print(f"PSNR 1 value is {value} dB")
compressed = cv2.imread("attacks/attack_s_p_image_w.png_2.png", 1)
value = PSNR(compressed,original )
print(f"PSNR 2 value is {value} dB")
compressed = cv2.imread("attacks/attack_s_p_image_w.png_3.png", 1)
value = PSNR(compressed,original )
print(f"PSNR 3 value is {value} dB")
compressed = cv2.imread("attacks/attack_s_p_image_w.png_4.png", 1)
value = PSNR(compressed,original )
print(f"PSNR 4 value is {value} dB")
#print("attack_s_p_image_w")
#compressed = cv2.imread(attack_s_p_image_w, 1)
#value = PSNR(compressed,original)
#print(f"PSNR value is {value} dB")

#print("attack_poisson_image_w")
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
