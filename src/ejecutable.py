from clases import *
matriz= []

def mostrarMatriz():
    
    """
    Esta función imprime la matriz en un formato de 6x6
    
    """    
    
    print("La matriz ingresada es:\n")
    for x in matriz:
        print(" ".join(x))
        
#Input de matriz 
def ingresarADN():
    global matriz  # Declarar matriz como global para modificarla
    matriz = []  # Reiniciar matriz al ingresar ADN
    for i in range(6):
        while True:
            fila = input(f"Ingrese la fila {i + 1} de la matriz (6 caracteres)> ").strip().upper()
            if len(fila) == 6 and all(base in 'ATCG' for base in fila):
                matriz.append(list(fila))
                  
                break 
            else:
                print("--ERROR--")

def menu():
    global matriz
    print("Ingrese un ADN que contenga las 4 bases nitrogenadas (una fila a la vez)\nAdenina (A), Timina (T), Citosina (C) y Guanina (G)")
    ingresarADN()
  
    #Menu
    mostrarMatriz() 
    while True: 
        print("¿Que desea hacer?\n1. Detectar mutaciones\n2. Mutar\n3. Sanar\n4. Mostrar la matriz")
        opcionU = int(input("Seleccione una opción: "))
        
        match opcionU:
            case 1: 
                print("--Se llama a la funcion para detectar mutaciones--")
                ADNU=Detector(matriz)
                TipoM = ADNU.detectar_mutantes()
                print(TipoM)
                
            case 2: 
                    mutacion = input("\nElija la base Nitrogenada que desae insertar: (A,T,C,G)>").upper()
    
                    #Evaluación de que la base ingresada sea correcta.
                    while True:
                        if not re.match("^([ATGC]*)$",mutacion):
                            print("El dato ingresado es incorrecto, vuelva a intentarlo")
                            mutacion = input("Elija la base Nitrogenada que desae insertar: (A,T,C,G)>").upper()
                                
                        else:
                            base_nitrogenada = mutacion
                            print(f"La base nitrogenada ingresada es {base_nitrogenada}.")
                            break
                    
                    print("\ningrese la posicion inicial en donde desea insertar la mutacion")
                    print("debe ser un digito del 1 al 3")
                    while True:
                        try:
                            posicion_inicial=int(input())
                            if posicion_inicial==1 or posicion_inicial==2 or posicion_inicial==3:
                                posicion_inicial=posicion_inicial-1
                                break
                            else:
                                print("ingrese un valor del 1 al 3")
                            
                        except ValueError:
                            print("--ERROR: debe ingresar un valor valido--")
                            continue  
                    
                    #menu de seleccion de mutacion
                    print("\n¿que mutasion desea ingresar en su ADN?")       
                    print("1.   <<<Mutante Diagonal>>>")                
                    print("2.   <<<Mutante Vertical>>>")                
                    print("3.   <<<Mutante horizonta>>>")
                    while True:
                        try:
                            seleccionar_mutacion = int(input("Seleccione una opción: "))
                            break
                        except ValueError:
                            print("--ERROR: Debe ingresar un número válido--")
                            continue
                    
                    match seleccionar_mutacion:
                        case 1:
                            mutante_diagonal= Virus(matriz, base_nitrogenada)
                            matriz = mutante_diagonal.crear_mutante(matriz,posicion_inicial)
                            print("--Mutación diagonal aplicada correctamente--")
                        case 2:
                            
                            pass
                        case 3:
                            pass                       
            case 3: 
                ADNU = Sanador(matriz)
                print("--Se llama a la funcion para sanar mutaciones--")
               
            case 4: 
                mostrarMatriz()                
menu()
