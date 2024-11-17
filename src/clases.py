import re

class Mutador():
    adn_mutantre = ["A", "T", "C", "G"]
    adn_tamanio = ""
    mutacion = ""
    
    #Ingreso de la base que se repetirá en la mutación.
    base_nitrogenada = input("""
                             Elija la base nitrogenada que desea insertar: 
                             Adenina (A), Timina (T), Citosina (C) y Guanina (G).
                             >""").upper()
    
    #Evaluación de que la base ingresada sea correcta.
    while True:
        if not re.match("^([ATGC]*)$",base_nitrogenada):
            print("""El dato ingresado es incorrecto, vuelva a intentarlo""")
            base_nitrogenada = input("""
                Elija la base nitrogenada que desea insertar: 
                Adenina (A), Timina (T), Citosina (C) y Guanina (G).
                >""").upper()
        else:
            print("Mutación ingresada correctamente")
            break
            
    #Método constructor
    def __init__(self, base_nitrogenada, adn_tamanio, mutacion):
        self.base_nitrogenada = base_nitrogenada
        self.adn_tamanio = adn_tamanio
        self.mutacion = mutacion
    
    def crear_mutante():
        pass
        
class Detector:
    #Metodo contrusctor donde se dividen los caracteres de cada fila para facilitar su analisis
    def __init__(self, matriz):
        self.matriz = [list(fila) for fila in matriz]

    def detectar_mutantes(self):
        # Llama a las funciones para detectar la mutacion
        return (self.Mut_horizontal() or self.mut_vertical() or self.mut_diagonalD() or self.mut_diagonalI())
                
    def Mut_horizontal(self):
        #Recorre cada fila individual buscando el caracter que se repita 4 veces
        for fila in self.matriz:
            #El -3 es para evitar desbordamiento, ya que el codigo busca 3 posiciones por delante en la que este el bucle
            #Por eso el maximo es la posicion 2, así 3 posiciones por delante llega al 3 y no intenta acceder a una posicion
            #que no existe
            for i in range(len(fila) - 3):  
                if fila[i] == fila[i+1] == fila[i+2] == fila[i+3]:
                    return "Mutacion horizontal"
        return None
    
    def mut_vertical(self):
        #El primer bucle se ubica en los caracteres de la primera fila, de esta forma recorre columna por columna
        for col in range(len(self.matriz[0])):  #El 0 es para que cuente unicamente la primera fila o primero sublista
            #Una vez ubicada en la columna por el bucle anterior recorre las posiciones para abajo
            for fil in range(len(self.matriz) - 3): 
                if (self.matriz[fil][col] == self.matriz[fil+1][col] ==
                    self.matriz[fil+2][col] == self.matriz[fil+3][col]):
                    return "Mutacion vertical"
        return None

    def mut_diagonalD(self):
        #En este caso empieza contando las filas -3 por el desbordamiento
        for fil in range(len(self.matriz)-3):  
            #Y cuenta los caracteres de cada fila, asignando las columnas 
            for col in range(len(self.matriz[0]) - 3):
                #De esta forma se pueden asignar los valores y recorre cada posicion de la matriz en diagonal
                if (self.matriz[fil][col] == self.matriz[fil+1][col+1] ==
                    self.matriz[fil+2][col+2] == self.matriz[fil+3][col+3]):
                    return "Mutacion Diagonal Derecha"
        return None
    
    def mut_diagonalI(self):
        #Mimso caso que la anterior pero al revez, ya que tiene el limite de 3
        for row in range(len(self.matriz) - 3):
            #Como tiene que recorrerla al reves empieza 3 posiciones por delante
            for col in range(3, len(self.matriz[0])):
                #Se resta en ves de sumar así va de izquierda a derecha en las columnas
                if (self.matriz[row][col] == self.matriz[row+1][col-1] ==
                    self.matriz[row+2][col-2] == self.matriz[row+3][col-3]):
                    return "Mutación Diagonal Izquierda"
        return None

class Radiacion(Mutador):
    pass

class Virus(Mutador):
    pass

class Sanador():
    pass

