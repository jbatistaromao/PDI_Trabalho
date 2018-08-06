import cv2
import matplotlib.pyplot as plt
import numpy as np
import scipy
from skimage.io import imread
from scipy import ndimage
from collections import deque
from scipy import signal as sg
from kMedias import KMedias
from referenciasImagens import ReferenciasImagens
   
def main():
    
    imagensDroga = ReferenciasImagens()

    testeKmedias = KMedias(imagensDroga.alprazolam)
    testeKmedias.allImages()

  
    '''
    imgpath =    'imagens remedio\\\\Medium Cut\\\\4607_lg.jpg'
   
       
      
   
    img = cv2.imread(imgpath, 0)
    img = (img * 255).round().astype(np.uint8)
    
    media = [[1./9., 1./9., 1./9.], 
                [1./9., 1./9., 1./9.], 
                [1./9., 1./9., 1./9.]]

    gausianoMultiplySix = [[1., 1., 1.], 
                            [1., 2., 1.], 
                            [1., 1., 1.]]

    passaBaixa = [[0., 1., 0.], 
                    [1., 1., 1.], 
                    [0., 1., 0.]]
       
      
    img = sg.convolve(img, gausianoMultiplySix, "valid")
     
    img = sg.convolve(img, media, "valid")

    Z = img.reshape((-1,1))
    print Z
    Z = np.float32(Z)
   
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1000.0)
    
    K=2
    ret, label1, center1 = cv2.kmeans(Z, K, None,
                                      criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output1 = res1.reshape((img.shape))
    cv2.imshow('output', output1)
    print output1
    print np.amax(output1)
    print np.amin(output1)
    
    K=4
    ret, label1, center1 = cv2.kmeans(Z, K, None,
                                      criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output2 = res1.reshape((img.shape))
    
    K=12
    ret, label1, center1 = cv2.kmeans(Z, K, None,
                                      criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center1 = np.uint8(center1)
    res1 = center1[label1.flatten()]
    output3 = res1.reshape((img.shape))

    output = [img, output1, output2, output3]
    titles = ['Original Image', 'K=2', 'K=4', 'K=12']
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()
    '''

if __name__ == "__main__":
    main()