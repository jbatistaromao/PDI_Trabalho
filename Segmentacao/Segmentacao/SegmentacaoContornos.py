import cv2
import numpy as np

#funcao identifica se ha uma pilula circular 
#retorna coordenada x e y do ponto central e o raio do circulo
#caso nao haja uma pilula circular retorna 0 para todos os valores
def contemPilulaCircular(imageUrl):
    #carrega e trata a imagen antes de aplicar a transformada de hough
    img = cv2.imread(imageUrl,0)
    img = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

    #gera o vetor de circulos achados na imagem
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

    
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)


    if len(circles) > 2:
        print 'Nao Possui pilula circular'
        return 0,0,0
    elif len(circles) == 1:
        #se a imagem possui uma pilula, o centro da pilula esta proximo ao centro da imagem
        w, h = img.shape
        if(w/2 - w*0.1 <= circles[0][0][0] <= w/2 + w*0.1 and h/2 - h*0.1 <= circles[0][0][1] <= h/2 + h*0.1):
            print 'tem circulo'
            cv2.imshow('detected circles',cimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            return circles[0][0][0], circles[0][0][1], ircles[0][0][2]
        print 'teste' 
        print w/2
        print h/2
        print circles

        
        cv2.imshow('detected circles',cimg)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


contemPilulaCircular('imagens remedio\\Medium cut\\3026_lg.jpg')