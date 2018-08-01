import matplotlib.pyplot as plt
import numpy as np
from skimage.io import imread

img = imread('3665_lg.tiff', as_grey=True)
img = (img * 255).round().astype(np.uint8)

fig = plt.figure(figsize=(7,7), dpi=50)
# mostra imagem
a = fig.add_subplot(1,2,1)
a.imshow(img, cmap=plt.cm.gray)
a.axis('off')
a.set_title('Original')

# mostra histograma
a = fig.add_subplot(1,2,2)
a.hist(img, bins=40, fc='k', ec='k')
a.set_title('Histograma')

plt.show()

# Calcula a média dos pixels da imagem
media = np.mean(img)
print(media)

# limiarização, limiar = media
bin = ((img>media)*255).astype("uint8")

fig = plt.figure(figsize=(7,7), dpi=50)
a = fig.add_subplot(1,3,1)
a.axis('off')
plt.imshow(img, cmap=plt.cm.gray)
a.set_title('Original')

a = fig.add_subplot(1,3,2)
a.axis('off')
plt.imshow(bin, cmap=plt.cm.gray)
a.set_title('Limiarização')

a = fig.add_subplot(1,3,3)
a.hist(img, bins=40, fc='k', ec='k')
a.axis('off')
a.axvline(media, linestyle='dashed', linewidth=1)
a.set_title('Histograma')

plt.show()

