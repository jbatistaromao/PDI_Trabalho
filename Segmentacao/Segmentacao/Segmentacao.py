

# Escreva o seu programa

def main():
   
    from FuncoesAuxiliares import Auxiliares
    from ReferenciasImagens import ReferenciasImagens
    from RegioesComSemente import RegioesComSemente
    ''' Cria objeto do tipo array de referencia '''
    imagensDroga = ReferenciasImagens()
  
    testeSemente = RegioesComSemente(imagensDroga.alprazolam)
   
    testeSemente.allImages()




    #funcAuxiliares = Auxiliares(imagensDroga.alprazolam)
    #funcAuxiliares.imprimirArray()
    
  

    
 
    print("Vixe! Ainda nao fiz este problema!")


#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main()