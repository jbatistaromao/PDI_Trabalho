
def main():
    import numpy as np
    #from FuncoesAuxiliares import Auxiliares
    from referenciasImagens import ReferenciasImagens
    from RegioesComSemente import RegioesComSemente
    from SegmentacaoContornos import contemPilulaCircular
    ''' Cria objeto do tipo array de referencia '''
    imagensDroga = ReferenciasImagens()
    
    #Caracteristicas dos objetos
    circularidade = 0
    areaMedia = 0
    areaAtual = 0
    perimetroMedio = 0
    perimetroAtual = 0

    qtdImagens = len(imagensDroga.alprazolam) + len(imagensDroga.domino) +\
                            len(imagensDroga.mediumCut) + len(imagensDroga.tesla) + len(imagensDroga.warnerBros)
    for i in range(qtdImagens):
        if i < len(imagensDroga.alprazolam):
            print ''
            _,_,raio = contemPilulaCircular(imagensDroga.alprazolam[i])
            if raio != 0:
                print 'Area atual: ' + str(3.14*raio*raio)
                print 'Perimetro atual: ' + str(3.14*2*raio)
                areaMedia = areaMedia + 3.14*raio*raio
                perimetroMedio = perimetroMedio + 2*3.14*raio
            else:
                testeSemente1.calcularAreaDroga(i)

    ''' print'########### ALPRAZOLAM ###########'
    testeSemente1 = RegioesComSemente(imagensDroga.alprazolam)
    testeSemente1.allImages()

    print'########### DOMINO ###########'
    testeSemente1 = RegioesComSemente(imagensDroga.domino)
    testeSemente1.allImages()
    '''
    print'########### MEDIUM CUT ###########'
    testeSemente1 = RegioesComSemente(imagensDroga.mediumCut)
    testeSemente1.allImages()
    '''
    print'########### TESLA ###########'
    testeSemente1 = RegioesComSemente(imagensDroga.tesla)
    testeSemente1.allImages()
   
    
    print'########### WARNER BROS ###########'
    testeSemente1 = RegioesComSemente(imagensDroga.warnerBros)
    testeSemente1.allImages()
    '''
    
    
    imagensDroga = ReferenciasImagens()

    testeKmedias = KMedias(imagensDroga.alprazolam)
    testeKmedias.allImages()

    
 
    print("Vixe! Ainda nao fiz este problema!")


#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main()