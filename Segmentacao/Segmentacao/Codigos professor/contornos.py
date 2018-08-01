
#Aqui tem sobel
from skimage import data
from scipy import misc
from scipy import signal as sg
import matplotlib.pyplot as plt
import numpy as np

#imagem = data.camera()
imagem = misc.imread('3095_lg.tiff', mode='L')

fig = plt.figure(figsize=(10,10), dpi=100)
a = fig.add_subplot(1,2,1)
plt.imshow(imagem, cmap=plt.cm.gray)
a.set_title('Original')
plt.tight_layout()
plt.axis('off')
plt.show()


sobel_x = [[-1, -2, -1], [0,0,0], [1,2,1]]
sobel_y = [[-1, 0,  1], [-2, 0, 2], [-1, 0, 1]]

c_sbl_x  = sg.convolve(imagem, sobel_x, "valid")
c_sbl_y  = sg.convolve(imagem, sobel_y, "valid")
c_sbl_xy = np.abs(c_sbl_x) + np.abs(c_sbl_y)

c_sbl = np.sqrt(c_sbl_x**2 + c_sbl_y**2)

fig = plt.figure(figsize=(10,10), dpi=100)
a = fig.add_subplot(2,2,1)
plt.imshow(c_sbl_x, cmap=plt.cm.gray)
a.set_title('Sobel x')

a = fig.add_subplot(2,2,2)
plt.imshow(c_sbl_y, cmap=plt.cm.gray)
a.set_title('Sobel y')

a = fig.add_subplot(2,2,3)
plt.imshow(c_sbl_xy, cmap=plt.cm.gray)
a.set_title('Sobel x+y')

a = fig.add_subplot(2,2,4)
plt.imshow(c_sbl, cmap=plt.cm.gray)
a.set_title('Sobel')


plt.show()

dif = c_sbl - c_sbl_xy

fig = plt.figure(figsize=(10,10), dpi=100)
a = fig.add_subplot(1,3,1)
plt.imshow(c_sbl_xy, cmap=plt.cm.gray)
a.set_title('Sobel x+y')

a = fig.add_subplot(1,3,2)
plt.imshow(c_sbl, cmap=plt.cm.gray)
a.set_title('Sobel')

a = fig.add_subplot(1,3,3)
plt.imshow(dif, cmap=plt.cm.gray)
a.set_title('Diferença')

plt.show()
