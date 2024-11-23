import re

class Mutador():
    adn_mutantre = ["A", "T", "C", "G"]
    base_nitrogenada = " "
            
    #Método constructor
    def __init__(self, base_nitrogenada):
        self.base_nitrogenada = base_nitrogenada
    def crear_mutante(self, matriz):
        pass
        
class Detector:
    def __init__(self, matriz):
        self.matriz = [list(fila) for fila in matriz]

    def detectar_mutantes(self):
        if((self.Mut_horizontal() or self.mut_vertical() or self.mut_diagonalD() or self.mut_diagonalI())):
            return True
        return False
    def Mut_horizontal(self):
        for fila in self.matriz:
            """
                El -3 es para evitar desbordamiento, ya que el código busca 3 posiciones por delante en la que esté el bucle
                Por eso el máximo es la posición 2, así 3 posiciones por delante llega al 3 y no intenta acceder a una posición
                que no existe
            """    
            for i in range(len(fila) - 3):  
                if fila[i] == fila[i+1] == fila[i+2] == fila[i+3]:
                    return True
        return False
    def mut_vertical(self):
        for col in range(len(self.matriz[0])):  
            for fil in range(len(self.matriz) - 3): 
                if (self.matriz[fil][col] == self.matriz[fil+1][col] ==
                    self.matriz[fil+2][col] == self.matriz[fil+3][col]):
                    return True
        return False

    def mut_diagonalD(self):
        for fil in range(len(self.matriz)-3):  
            for col in range(len(self.matriz[0]) - 3):
                if (self.matriz[fil][col] == self.matriz[fil+1][col+1] ==
                    self.matriz[fil+2][col+2] == self.matriz[fil+3][col+3]):
                    return True
        return False
    
    def mut_diagonalI(self):
        for row in range(len(self.matriz) - 3):
            for col in range(3, len(self.matriz[0])):
                if (self.matriz[row][col] == self.matriz[row+1][col-1] ==
                    self.matriz[row+2][col-2] == self.matriz[row+3][col-3]):
                    return True
        return False

class Radiacion(Mutador):
    
    def __init__(self, matriz, base_nitrogenada):
        super().__init__(base_nitrogenada)  
        self.matriz = matriz  
        
    def crear_mutanteV(self,matriz,posicion_inicial):
     self.matriz = matriz
      
     matriz_modificada = [list(fila) for fila in matriz]
     
     for i in range(posicion_inicial, min(posicion_inicial + 4, len(matriz_modificada))):
                matriz_modificada[i][posicion_inicial] = self.base_nitrogenada
     return ["".join(fila) for fila in matriz_modificada]

    
    def crear_mutanteH(self,matriz, posicion_inicial):
        self.matriz = matriz
        
        matriz_modificada = [list(fila) for fila in self.matriz]
            
        for i in range(posicion_inicial, min(posicion_inicial + 4, len(matriz_modificada))):
                matriz_modificada[posicion_inicial][i] = self.base_nitrogenada
        return ["".join(fila) for fila in matriz_modificada]

class Virus(Mutador):
    def __init__(self,matriz,base_nitrogenada):
        super().__init__(base_nitrogenada)  
        self.matriz = matriz  
    def crear_mutante(self, matriz, posicion_inicial):
        self.matriz = matriz
    
        matriz_modificada = [list(fila) for fila in matriz]
        for i in range(posicion_inicial, min(posicion_inicial + 4, len(matriz_modificada))):
            matriz_modificada[i][i] = self.base_nitrogenada

        self.matriz_mutante = ["".join(fila) for fila in matriz_modificada]
        return self.matriz_mutante
import random

class Sanador:
    def __init__(self):
        pass
    def sanar_mutantes(self,matriz):
         
        detector = Detector(matriz)
        if detector.detectar_mutantes():
            nueva_matriz = self.generar_adn_aleatorio()
            while detector.detectar_mutantes == True:
                nueva_matriz = self.generar_adn_aleatorio()
            return nueva_matriz
        return matriz
    def generar_adn_aleatorio(self):
      
        bases = ["A", "T", "C", "G"]
        nueva_matriz = []
        for _ in range(6):
            fila = ''.join(random.choice(bases) for _ in range(6))
            nueva_matriz.append(fila)
        return nueva_matriz
    

