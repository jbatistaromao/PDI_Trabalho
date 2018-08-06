import matplotlib.pyplot as plt
import scipy
import numpy as np
from skimage.io import imread
from scipy import ndimage
from collections import deque
from scipy import signal as sg


class RegioesComSemente():
      imagensDrogas = []
      area
      def __init__(self, imagens):
        self.imagensDrogas = imagens
        


      def obterSemente(self,image, posicaopirula):

        # Sabemos que a pilula esta sempre no centro da imagem
        # A semente sera um retangulo no centro
        larguraImagem, alturaImagem = image.shape
        
        if posicaopirula == 'centro':
            p = 10. # p e uma porcentagem da altura e da largura
            pos_ini_x_mrk = int(larguraImagem/2 - p*larguraImagem/100.)
            pos_ini_y_mrk = int(alturaImagem/2 - p*alturaImagem/100.)
            pos_fim_x_mrk = int(larguraImagem/2 + p*larguraImagem/100.)
            pos_fim_y_mrk = int(alturaImagem/2 + p*alturaImagem/100.)
        else:
            larguraSemente = 11
            pos_ini_x_mrk = int(1)
            pos_ini_y_mrk = int(1)
            pos_fim_x_mrk = int(larguraSemente)
            pos_fim_y_mrk = int(larguraSemente)

        # Semente e uma imagem do mesmo tamanho que img, contendo zeros
        semente = np.zeros(shape=(larguraImagem,alturaImagem), dtype=np.uint8)
        # acrescenta um retangulo central de pixels = 255
        semente[pos_ini_x_mrk:pos_fim_x_mrk, pos_ini_y_mrk:pos_fim_y_mrk] = 255
    
        return semente

      def vizinhos(self,x, y, w, h):

        lista = deque()
    
        pontos = [(x-1,y), (x+1, y), (x,y-1), (x,y+1),
                  (x-1,y+1), (x+1, y+1), (x-1,y-1), (x+1,y-1),
                 ]
        for p in pontos:
            if (p[0]>=0 and p[1]>=0 and p[0]<w and p[1]<h):
                lista.append((p[0], p[1]))
            
        return lista

      def crescerRegiao(self,image, reg, epsilon=4):
        w, h = image.shape
    
        fila = deque()
        for x in range(w):
            for y in range(h):
                if reg[x,y]==255:
                    fila.append((x,y))
       
        while fila:
            ponto = fila.popleft()
            x = ponto[0]
            y = ponto[1]

            v_list = self.vizinhos(x, y, w, h)
            for v in v_list:
                v_x = v[0]
                v_y = v[1]
                if( (reg[v_x][v_y]!=255) and (abs(image[x][y]-image[v_x][v_y])<epsilon)):
                    reg[v_x][v_y] = 255
                    fila.append((v_x,v_y))
        return reg

      def plots(self,p1, p2):
        
        
        fig = plt.figure(figsize=(9,3), dpi=80)
        a = fig.add_subplot(1,3,1)
        a.axis('off')
        plt.imshow(p1, cmap=plt.cm.gray)
        a.set_title('Original')

        a = fig.add_subplot(1,3,2)
        a.axis('off')
        plt.imshow(p2, cmap=plt.cm.gray)
        a.set_title('Cresc.Regiao')

        a = fig.add_subplot(1,3,3)
        a.axis('off')
        plt.imshow(p1, cmap=plt.cm.gray)
        plt.imshow(p2, alpha=0.5)
        a.set_title('Cresc.Regiao')

        plt.show()

      def segmentarImage(self, numeroImagem):
        # Leitura Imagem
        
        img1 = imread(self.imagensDrogas [numeroImagem], as_grey=True)
        img1 = (img1 * 255).round().astype(np.uint8)

        posicaoPirula= self.verificarPosicaoDroga(img1)

        semente = self.obterSemente(img1,posicaoPirula)

        

        media = [[1./9., 1./9., 1./9.], 
                  [1./9., 1./9., 1./9.], 
                  [1./9., 1./9., 1./9.]]

        gausianoMultiplySix = [[1., 1., 1.], 
                               [1., 2., 1.], 
                               [1., 1., 1.]]

        passaBaixa = [[0., 1., 0.], 
                      [1., 1., 1.], 
                      [0., 1., 0.]]
       
        
        
        contrast   = 4
        brightness = 3

        #c_media = img1*(contrast/127 + 1) - contrast + brightness
      
        c_media = sg.convolve(img1, gausianoMultiplySix, "valid")
     
        c_media = sg.convolve(c_media, media, "valid")
        
       
        if posicaoPirula == 'centro':
                regiao = self.crescerRegiao(c_media, semente, epsilon=55.0)
        else:
                regiao = self.crescerRegiao(c_media, semente, epsilon=22.5)

        self.plots(c_media, regiao)
     
      def allImages(self):
          
          for i in range(len(self.imagensDrogas)):
         
            self.segmentarImage(i)

      def verificarPosicaoDroga(self,image):
          larguraImagem, alturaImagem = image.shape

          borda =  [image[0][0],image[0][1],image[0][2],image[1][0],image[1][1],image[1][2],image[2][0],image[2][1],image[2][2]]
          centro = [image[(larguraImagem/2) - 1][(alturaImagem/2) - 1],  image[(larguraImagem/2) - 1][(alturaImagem/2)],  image[(larguraImagem/2) - 1][(alturaImagem/2) + 1],
                    image[(larguraImagem/2)][(alturaImagem/2) - 1],  image[(larguraImagem/2)][(alturaImagem/2)],  image[(larguraImagem/2)][(alturaImagem/2) + 1],
                    image[(larguraImagem/2) + 1][(alturaImagem/2) - 1],  image[(larguraImagem/2) + 1][(alturaImagem/2)],  image[(larguraImagem/2) +1 ][(alturaImagem/2) + 1],]
                    

          posicaoPirula = self.mediaCorSemente(borda, centro,10)
          return posicaoPirula

    
      def mediaCorSemente(self,borda, centro, epsilon):
          tipoFiltro = 'normal'
          posicaoPirula = ""
          mediaBorda = 0.0
          mediaCentro = 0.0

          for i in range(8):
              mediaBorda += borda[i]
              mediaCentro += centro[i]

          mediaBorda = mediaBorda/9
          mediaCentro = mediaCentro/9

         
          print mediaCentro
          diferenca = abs(mediaBorda - mediaCentro)

          if mediaBorda < 5:
            posicaoPirula = 'centro'
            print 1
          elif mediaBorda < 50:
            posicaoPirula = 'borda'
            print 2
          elif mediaCentro < mediaBorda:
            posicaoPirula = 'borda'
            print 3
          elif mediaCentro > mediaBorda:
            posicaoPirula = 'centro'
            print 5
          elif diferenca > 85.0:
            posicaoPirula = 'borda'
            print 5
          elif mediaCentro > 190:      
            posicaoPirula = 'borda' 
            print 6
          else:
            posicaoPirula = 'borda'   
            print 7
         
          return posicaoPirula
      def calcularAreaDroga(img):
          print'Area'


     
        