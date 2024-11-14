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
    #Falta agregar una cosa más de la funcion diagona, agregar comentarios explicando la logica y verificar todo en su conjunto
    def __init__(self, matriz):
        self.matriz = [list(fila) for fila in matriz]

    def detectar_mutantes(self):
        return (self.Mut_horizontal() or self.mut_vertical() or self.mut_diagonal())
                
    def Mut_horizontal(self):
        for fila in self.matriz:
            for i in range(len(fila) - 3):  
                if fila[i] == fila[i+1] == fila[i+2] == fila[i+3]:
                    return "Mutacion horizontal"
        return None
    
    def mut_vertical(self):
        for col in range(len(self.matriz[0])):  
            for fil in range(len(self.matriz) - 3):
                if (self.matriz[fil][col] == self.matriz[fil+1][col] ==
                    self.matriz[fil+2][col] == self.matriz[fil+3][col]):
                    return "Mutacion vertical"
        return None

    def mut_diagonal(self):
        for fil in range(len(self.matriz)-3):  
            for col in range(len(self.matriz[0]) - 3):
                if (self.matriz[fil][col] == self.matriz[fil+1][col+1] ==
                    self.matriz[fil+2][col+2] == self.matriz[fil+3][col+3]):
                    return "Mutacion Diagonal"
        return None
    

class Radiacion(Mutador):
    pass

class Virus(Mutador):
    pass

class Sanador():
    pass

