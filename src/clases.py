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
        #El primer bucle se ubica en los caracteres de la primera fila, de esta forma recorre columna por columna
        for col in range(len(self.matriz[0])):  #El 0 es para que cuente únicamente la primera fila o primera sublista
            #Una vez ubicada en la columna por el bucle anterior recorre las posiciones para abajo
            for fil in range(len(self.matriz) - 3): 
                if (self.matriz[fil][col] == self.matriz[fil+1][col] ==
                    self.matriz[fil+2][col] == self.matriz[fil+3][col]):
                    return True
        return False

    def mut_diagonalD(self):
        #En este caso empieza contando las filas -3 por el desbordamiento
        for fil in range(len(self.matriz)-3):  
            #Y cuenta los caracteres de cada fila, asignando las columnas 
            for col in range(len(self.matriz[0]) - 3):
                #De esta forma se pueden asignar los valores y recorre cada posición de la matriz en diagonal
                if (self.matriz[fil][col] == self.matriz[fil+1][col+1] ==
                    self.matriz[fil+2][col+2] == self.matriz[fil+3][col+3]):
                    return True
        return False
    
    def mut_diagonalI(self):
        #Mismo caso que la anterior pero al revés, ya que tiene el limite de 3
        for row in range(len(self.matriz) - 3):
            #Como tiene que recorrerla al revés, empieza 3 posiciones por delante
            for col in range(3, len(self.matriz[0])):
                #Se resta en vez de sumar así va de izquierda a derecha en las columnas
                if (self.matriz[row][col] == self.matriz[row+1][col-1] ==
                    self.matriz[row+2][col-2] == self.matriz[row+3][col-3]):
                    return True
        return False

class Radiacion(Mutador):
    pass


class Virus(Mutador):
    
    def __init__(self,matriz,base_nitrogenada):
        super().__init__(base_nitrogenada)  # Inicializa el constructor de la clase padre
        self.matriz = matriz  #matriz q usara para la mutacion
        
    def crear_mutante(self, matriz, posicion_inicial):
        self.matriz = matriz
      
        # Convertir las cadenas a listas de caracteres para poder modificarlas
        matriz_modificada = [list(fila) for fila in matriz]

           
        # Modificar la diagonal principal desde la posición inicial
        for i in range(posicion_inicial, min(posicion_inicial + 4, len(matriz_modificada))):
            matriz_modificada[i][i] = self.base_nitrogenada

            
        # Convertir de nuevo las listas de caracteres a cadenas
        self.matriz_mutante = ["".join(fila) for fila in matriz_modificada]

        
        # Imprimimos para verificar
        #for fila in self.matriz_mutante:
            #print(fila)

        
        #retornamos
        return self.matriz_mutante
    

class Sanador():
    pass

