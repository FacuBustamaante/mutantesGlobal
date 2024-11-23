from clases import *
matriz= []

def mostrarMatriz():
    """
    Esta función imprime la matriz en un formato de 6x6
    
    """    
    print("\nLa matriz ingresada es:\n")
    for x in matriz:
        print(" ".join(x))
        
#Input de matriz 
def ingresarADN():
    global matriz  
    matriz = []  
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
        print("\n¿Que desea hacer?\n\n1. Detectar mutaciones\n2. Mutar el ADN\n3. Sanar el ADN\n4. Mostrar la matriz ingresada")
        opcionU = int(input("\x1B[3mSeleccione una opción:\x1B[0m "))
                
        match opcionU:
            case 1: 
                ADNU=Detector(matriz)
                TipoM = ADNU.detectar_mutantes()
                  if(TipoM == True):
                    print("Se detecto una mutacion")
                  else: print("No se detectaron mutaciones")
                
            case 2: 
                    mutacion = input("\nElija la base Nitrogenada que desae insertar: (A,T,C,G)>").upper()
                    while True:
                        if not re.match("^([ATGC]*)$",mutacion):
                            print("El dato ingresado es incorrecto, vuelva a intentarlo")
                            mutacion = input("Elija la base Nitrogenada que desae insertar: (A,T,C,G)>").upper()
                        else:
                            base_nitrogenada = mutacion
                            print(f"La base nitrogenada ingresada es {base_nitrogenada}.")
                            break
                    
                    print("\nIngrese la posición inicial donde desea insertar la mutación\n(Debe ser un valor entre 1-3)")
                    while True:
                        try:
                            posicion_inicial=int(input())
                            if posicion_inicial==1 or posicion_inicial==2 or posicion_inicial==3:
                                posicion_inicial=posicion_inicial-1
                                break
                            else:
                                print("Por favor, ingrese un valor entre 1-3.")
                            
                        except ValueError:
                            print("--ERROR: debe ingresar un valor valido--")
                            continue
                    
                    #Selección de mutación
                    print("\n¿Que mutación desea ingresar en su ADN?\n1. Mutación Diagonal\n2. Mutación Vertical\n3. Mutación Horizontal")  
                         
                    while True:
                        try:
                            seleccionar_mutacion = int(input("Seleccione una opción: "))
                            break
                        except ValueError:
                            print("--ERROR: Debe ingresar un número válido--")
                            continue
                    
                    match seleccionar_mutacion:
                        case 1:
                            mutante_diagonal = Virus(matriz, base_nitrogenada)
                            matriz = mutante_diagonal.crear_mutante(matriz,posicion_inicial)
                            print("Mutación diagonal aplicada correctamente")
                        case 2:
                            #Mutante Vertical
                            mutante_vertical = Radiacion(matriz, base_nitrogenada)
                            matriz = mutante_vertical.crear_mutanteV(matriz,posicion_inicial)
                            print("Mutación vertical aplicada correctamente")
                        case 3:
                            #Mutante Horizontal
                            mutante_horizontal = Radiacion(matriz, base_nitrogenada)
                            matriz = mutante_horizontal.crear_mutanteH(matriz,posicion_inicial)
                            print("Mutación horizontal aplicada correctamente") 
            case 3: 
                sanador = Sanador()
                matriz = sanador.sanar_mutantes(matriz)
                print("ADN sanado correctamente")   
            case 4: 
                mostrarMatriz()                
menu()
