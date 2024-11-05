class Mutador():
    def __init__(self):
        print(self)
        
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

