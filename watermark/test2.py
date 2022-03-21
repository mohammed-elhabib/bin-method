from math import log10, sqrt

import cv2
import numpy as np

from bin_method import readImage, readImage2, printImage, extract_watermark
def PSNR(original, compressed):
    mse = np.mean((original - compressed) ** 2)
    if(mse == 0):  # MSE is zero means no noise is present in the signal .
                  # Therefore PSNR have no importance.
        return 100
    max_pixel = 255.0
    psnr = 20 * log10(max_pixel / sqrt(mse))
    return psnr
image_water_mark = "imag_host_1.png"

_,_,hostImage = readImage2(image_water_mark)

original = cv2.imread("w_l.png")


printImage(np.rot90(hostImage),"imag_host_90.png")
extract_watermark("imag_host_90.png","w_90.png")
print("90")
compressed = cv2.imread("w_90.png", 1)
value = PSNR(original, compressed)
print(f"PSNR value is {value} dB")


printImage(np.rot90(hostImage,2),"imag_host_180.png")
extract_watermark("imag_host_180.png","w_180.png")
print("180")
compressed = cv2.imread("w_180.png", 1)
value = PSNR(original, compressed)
print(f"PSNR value is {value} dB")

printImage(np.rot90(hostImage,3),"imag_host_270.png")
extract_watermark("imag_host_180.png","w_270.png")
print("270")
compressed = cv2.imread("w_270.png", 1)
value = PSNR(original, compressed)
print(f"PSNR value is {value} dB")