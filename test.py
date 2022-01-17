import numpy as np

from bin_method import readWaterImage, printImage

image_water_mark = "input/w.png"
watermark_size = 64
imag_w = readWaterImage(image_water_mark, watermark_size)
imag_w_p1 = imag_w[:32, :32]
imag_w_p2 = np.rot90(imag_w[32:64, :32],3)
imag_w_p3 = np.rot90(imag_w[:32, 32:64],2)
imag_w_p4 = np.rot90(imag_w[32:64, 32:64])
imag_w[:32, :32]=imag_w_p1
imag_w[32:64, :32]=imag_w_p2
imag_w[:32, 32:64]=imag_w_p3
imag_w[32:64, 32:64]=imag_w_p4

imag_w=np.rot90(imag_w)
printImage(imag_w,"test_w_image.png")

imag_w_p1 = imag_w[:32, :32]
imag_w_p2 = np.rot90(imag_w[32:64, :32],)
imag_w_p3 = np.rot90(imag_w[:32, 32:64],2)
imag_w_p4 = np.rot90(imag_w[32:64, 32:64],3)
imag_w[:32, :32]=imag_w_p1
imag_w[32:64, :32]=imag_w_p2
imag_w[:32, 32:64]=imag_w_p3
imag_w[32:64, 32:64]=imag_w_p4
printImage(imag_w,"test_w_image2.png")
