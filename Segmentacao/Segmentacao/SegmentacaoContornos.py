import cv2
import numpy as np
from matplotlib import pyplot as plt
import warnings

#funcao identifica se ha uma pilula circular 
#retorna coordenada x e y do ponto central e o raio do circulo
#caso nao haja uma pilula circular retorna 0 para todos os valores
def contemPilulaCircular(imageUrl):
    #carrega e trata a imagen antes de aplicar a transformada de hough

   
 
    #checa se e necessario ou nao aplicar o blur

    continuar = True
    parameter = 1


    while continuar == True:
        img = cv2.imread(imageUrl,0)
        img = cv2.medianBlur(img,parameter)
        cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=100,param2=30,minRadius=0,maxRadius=0)

 
        if circles is None:
            parameter = parameter - 2
            img = cv2.imread(imageUrl,0)
            img = cv2.medianBlur(img,parameter)
            cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

            circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=100,param2=30,minRadius=0,maxRadius=0)
            
            break

        if len(circles[0]) > 2:
            parameter = parameter + 2
        elif len(circles[0]) == 2:
            #distancia entre os circulos
            d = abs(int(circles[0][0][0]) - int(circles[0][1][0]))
            #raio dos circulos
            r1 = circles[0][0][2]
            r2 = circles[0][1][2]

            if ~(d - d*0.05 <= r1+r2 <= d + d*0.05):
                parameter = parameter + 2
            else:
               break
        else:
            continuar = False

        if parameter > 15:
            print 'Nao ha pilulas circulares'
            cv2.imshow('detected circles',cimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return 0,0,0



    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)



    
  

    if len(circles[0]) == 1:
        #se a imagem possui uma pilula, o centro da pilula esta proximo ao centro da imagem
        w, h = img.shape
        if(w/2 - w*0.1 <= circles[0][0][0] <= w/2 + w*0.1 and h/2 - h*0.1 <= circles[0][0][1] <= h/2 + h*0.1):
            print 'tem circulo'
            cv2.imshow('detected circles',cimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return circles[0][0][0], circles[0][0][1], circles[0][0][2]


        else:
            print 'Nao tem pilulas circulares'
            cv2.imshow('detected circles',cimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return 0,0,0

    elif len(circles[0]) == 2:

        #distancia entre os circulos
        d = abs(int(circles[0][0][0]) - int(circles[0][1][0]))
        #raio dos circulos
        r1 = circles[0][0][2]
        r2 = circles[0][1][2]
        
        if(d - d*0.05 <= r1+r2 <= d + d*0.05):
            print 'possui duas pilulas circulares'

            cv2.imshow('detected circles',cimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            x = [circles[0][0][0],circles[0][1][0]]
            y = [circles[0][0][1],circles[0][1][1]]
            raio = [circles[0][0][2], circles[0][1][2]]
            return x,y,raio
        else: 
            print 'Nao possui pilula circular'
            cv2.imshow('detected circles',cimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            return 0,0,0


    else:
        print 'Nao ha circulos'
        cv2.imshow('detected circles',cimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
           
        return 0,0,0


