

# Escreva o seu programa

def main():
   
    from FuncoesAuxiliares import Auxiliares
    from referenciasImagens import ReferenciasImagens
    from Regioes import regiao
    ''' Cria objeto do tipo array de referencia '''
    imagensDroga = ReferenciasImagens()





    funcAuxiliares = Auxiliares(imagensDroga.alprazolam)
    funcAuxiliares.imprimirArray()
    
    segmentoPorRegioes = regiao(imagensDroga.alprazolam)

    
 
    print("Vixe! Ainda nao fiz este problema!")


#-----------------------------------------------------
if __name__ == '__main__': # chamada da funcao principal
    main()