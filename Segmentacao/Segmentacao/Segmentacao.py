

# Escreva o seu programa



# Escreva o seu programa

def main():
    import numpy as np
    from FuncoesAuxiliares import Auxiliares
    from referenciasImagens import ReferenciasImagens
    from RegioesComSemente import RegioesComSemente
    ''' Cria objeto do tipo array de referencia '''
    imagensDroga = ReferenciasImagens()
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
  

    
 
    print("Vixe! Ainda nao fiz este problema!")


#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main()