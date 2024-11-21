from clases import *
matriz= []

#Input de matriz 
def ingresarADN():
 for i in range(6):
    while True:
        fila = input(f"Ingrese la fila {i + 1} de la matriz (6 caracteres)> ").strip().upper()
        if len(fila) == 6 and all(base in 'ATCG' for base in fila):
            matriz.append(list(fila))  
            break 
        else:
            print("--ERROR--")

def menu():
    print("""
        Ingrese un ADN que contenga las 4 bases nitrogenadas (una fila a la vez)
        (Adenina (A), Timina (T), Citosina (C) y Guanina (G))
        --EJEMPLO--
        TTTTCA, GATTCA, CAACAT, GAGCTA, ATTGCG, CTGTTC
        --EJEMPLO
        """)
    ingresarADN()
    
    #Menu
   # print(f"La matriz ingresada es: ")
    #for x in matriz:
     #   print(x)
    while True: 
        print("""
            --MENU--
            1. Detectar si hay mutaciones en el ADN
            2. Mutar ADN
            3. Sanar ADN
            4. Mostrar ADN ingresado
            --MENU--
            """)
        opcionU = int(input("Seleccione una opción: "))
        
        match opcionU:
            case 1: 
                print("--Se llama a la funcion para detectar mutaciones--")
                ADNU=Detector(matriz)
                TipoM = ADNU.detectar_mutantes()
                if TipoM:
                    print(f"Se detectó una {TipoM} en el ADN.")
                    #print(f" ".join(matriz[0]), "\n", " ".join(matriz[1]))
                else:
                    print("No se detectaron mutaciones en el ADN.")
                
            case 2: 
                    mutacion = input("""
                                Elija la base nitrogenada que desea insertar: 
                                Adenina (A), Timina (T), Citosina (C) y Guanina (G).
                                >""").upper()
    
                    #Evaluación de que la base ingresada sea correcta.
                    while True:
                        if not re.match("^([ATGC]*)$",mutacion):
                            print("""El dato ingresado es incorrecto, vuelva a intentarlo""")
                            mutacion = input("""
                                Elija la base nitrogenada que desea insertar: 
                                Adenina (A), Timina (T), Citosina (C) y Guanina (G).
                                >""").upper()
                        else:
                            base_nitrogenada = mutacion * 4
                            print(f"La base nitrogenada ingresada es {base_nitrogenada}.")
                            print("Mutación ingresada correctamente")
                            break
                    
                    
                    #menu de seleccion de mutacion
                    print("""
                                ¿que mutasion desea ingresar en su ADN?
                            <<<seleccione un numero para indicar su accion>>>
                                    1.Mutante Diagonal
                                    2.Mutante Vertical
                                    3.Mutante horizontal
                          
                          """)
                    seleccionar_mutacion=int(input())
                    match seleccionar_mutacion:
                        case 1:
                            mutante_diagonal=Virus()
                            mutante_diagonal.crear_mutante(matriz,base_nitrogenada,0)
                            matriz=mutante_diagonal.matriz_mutante
                        case 2:
                            
                            pass
                        case 3:
                            pass
                        
                        
            case 3: 
                ADNU = Sanador(matriz)
                print("--Se llama a la funcion para sanar mutaciones--")
               
            case 4: 
                print("--Se imprime el ADN ingresado--")
                print(matriz)
menu()

