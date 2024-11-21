
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
        for fila in self.matriz_mutante:
            print(fila)

        
        #retornamos
        return self.matriz_mutante
