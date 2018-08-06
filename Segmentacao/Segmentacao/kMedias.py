import cv2
import matplotlib.pyplot as plt
import numpy as np
import scipy
from skimage.io import imread
from scipy import ndimage
from collections import deque
from scipy import signal as sg

class KMedias():
 
      imagensDrogas = []

      def __init__(self, imagem):
        self.imagensDrogas = imagem

      def criarImagemParaCalculoDeArea(self, img):
        larguraImagem, alturaImagem = img.shape
        corFundo = 0
        corDroga = 0
        if img [0] [0]  ==  np.amax(img):
            corDroga = np.amax(img)
            corFundo = np.amin(img)
        else:
            corDroga = np.amax(img)
            corFundo = np.amin(img)
        for i in range(larguraImagem):
            for j in range (alturaImagem):
                if(img [i][j] == corFundo):
                    img [i][j] = 0
                else:
                    img [i][j] = 255
       
        return img
      
      def segmentarImage(self, numeroImagem):
        #Leitura Imagem
        
        img = cv2.imread(self.imagensDrogas [numeroImagem], 0)
        
        
        # Convertendo matriz para array, do tipo float32 para ser recebido no criterio
        Z = img.reshape((-1,1))
        Z = np.float32(Z)
        #Criterio e  o criterio de terminacao de iteracao 
        #cv2.TERM_CRITERIA_EPS interrompe a iteracao do algoritmo se a precisao especificada, epsilon , 
        #for atingida. cv2.TERM_CRITERIA_MAX_ITER - interrompe o algoritmo apos o numero especificado 
        #de iteracoes, max_iter . cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER - interro
        # quando qualquer uma das condicoes acima e atendida.
        # 10 e o numero maximo de interacoes e 100 o epslon
        criterio = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 1.0)
        
        #dois porque queremos diferenciar o fundo da droga
        K=2
        ret, label1, center1 = cv2.kmeans(Z, K, None, criterio, 10, cv2.KMEANS_RANDOM_CENTERS)
        #Matriz do centro dos clusters
        center1 = np.uint8(center1)
        #A soma da distancia ao quadrado de cada ponto para seus centros correspondentes.
        res1 = center1[label1.flatten()]
        #variavel que recebe a matriz de saida, a matriz e reorganizada
        output1 = res1.reshape((img.shape))
       

        #imprime
        self.plots(img, output1)
        #Pegar essa imagem para calculo da area e perimetro.
        imgBinaria = self.criarImagemParaCalculoDeArea(output1)
        

      def plots(self,imagemdroga, imagemKmedia):

        imagemdroga = np.array(imagemdroga, dtype = float)
        imagemKmedia = np.array(imagemKmedia, dtype = float)

        fig = plt.figure(figsize=(9,3), dpi=80)
        a = fig.add_subplot(1,2,1)
        a.axis('off')
        plt.imshow(imagemdroga,cmap=plt.cm.gray)
        a.set_title('Original')

        a = fig.add_subplot(1,2,2)
        a.axis('off')
        plt.imshow(imagemKmedia,cmap=plt.cm.gray)
        a.set_title('Kmedias')

        plt.show()
        
      def allImages(self):
        for i in range(len(self.imagensDrogas)):
            self.segmentarImage(i)

        
   

      