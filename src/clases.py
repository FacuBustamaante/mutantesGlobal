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
        
class Detector():
    nombre = "facundo"
    
    def __init__(self):
        print("Detector")
    
    def __str__(self):
        return f"nombre: {self.nombre}"

class Radiacion(Mutador):
    pass

class Virus(Mutador):
    pass

class Sanador():
    pass

