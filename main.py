from math import log10, sqrt

import cv2
import numpy as np

from attack2 import noisy
from bin_method import embedd_watermark, extract_watermark, printImage, readImage, readWaterImage

image_host = "input/1.jpg"
image_water_marked = "imag_host_1.png"
image_water_mark = "input/w.png"
image_water_mark_extract = "mark_extract.png"
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
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr

original = cv2.imread("w_l.png")

print("attack_gauss_image_w")
compressed = cv2.imread(attack_gauss_image_w, 1)
value = PSNR(original, compressed)
print(f"PSNR value is {value} dB")

print("image_water_mark_extract")
compressed = cv2.imread(image_water_mark_extract, 1)
value = PSNR(original, compressed)
print(f"PSNR value is {value} dB")
print("attack_s_p_image_w")
compressed = cv2.imread(attack_s_p_image_w, 1)
value = PSNR(original, compressed)
print(f"PSNR value is {value} dB")

print("attack_poisson_image_w")
compressed = cv2.imread(attack_poisson_image_w, 1)
value = PSNR(original, compressed)
print(f"PSNR value is {value} dB")

print("attack_speckle_image_w")
compressed = cv2.imread(attack_speckle_image_w, 1)
value = PSNR(original, compressed)
print(f"PSNR value is {value} dB")

print("attack_speckle_image_w")
compressed = cv2.imread(attack_speckle_image_w, 1)
value = PSNR(original, compressed)
print(f"PSNR value is {value} dB")
