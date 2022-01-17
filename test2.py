import numpy as np

image_water_mark = "input/w.png"
watermark_size = 62
imag_image = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [10, 20, 30, 40], [50, 60, 70, 80]])

imag_w_all=np.zeros((8,8))
imag_w_all[:4,:4]=np.copy(imag_image)
imag_w_all[:4,4:]=np.rot90(np.copy(imag_image),3)
imag_w_all[4:, :4]=np.rot90(np.copy(imag_image),1)
imag_w_all[4:,4:]=np.rot90(np.copy(imag_image),2)

#print(imag_w_all)
print(np.rot90(imag_w_all,1))
print(np.rot90(imag_w_all,2))
print(np.rot90(imag_w_all,3))
#print(np.rot90(imag_w_all,3))