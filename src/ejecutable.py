from clases import  Detector, Mutador, Radiacion, Virus, Sanador

"""
Hay cosas por modificar a medida que se vayan haciendo el resto de clases
Se que la detector tiene que dar un booleano pero lo hice de esta forma así en un futuro
se si lo esta detectando bien, cuando me asegure de eso lo cambio a booleano para que solo de V o F
"""
matriz= []
#La funcion pide al usuario que ingrese el ADN mediante un bucle, de esta forma lo puede hacer fila por fila
def ingresarADN():
 for i in range(6):
    while True:
        #Le pide al usuario que ingrese la fila correspondiente del ADN, elimina espacios en blanco
        #y hace todo a mayusculas
        fila = input(f"Ingrese la fila {i + 1} de la matriz (6 caracteres)> ").strip().upper()
        #Comprueba que lo ingresado sea de 6 caracteres y sean los caracteres correctos
        if len(fila) == 6 and all(base in 'ATCG' for base in fila):
            #Agrega a la matriz cada fila ingresado por el usuario como una lista
            #De esta forma la matriz es una lista de cada fila que contiene una lista con los caracteres
            matriz.append(list(fila))  
            break 
        else:
            print("--ERROR--")

#Es el menu en si, se le explica al usuario como, que ingresar y se le da un ejemplo
def menu():
    print("""
    Ingrese un ADN que contenga las 4 bases nitrogenadas (una fila a la vez)
    (Adenina (A), Timina (T), Citosina (C) y Guanina (G))
    --EJEMPLO--
    TTTTCA, GATTCA, CAACAT, GAGCTA, ATTGCG, CTGTTC
    --EJEMPLO
    """)
    #se llama a la funcion para que ingrese el ADN
    ingresarADN()
    #Una vez terminado de ingresar el ADN se le muestra un menu para que indique que desee hacer con ese ADN
    while True: 
        print("""
    --MENU--
    1: Detectar si hay mutaciones en el ADN
    2:Mutar ADN
    3:Sanar ADN
    4:Mostrar ADN ingresado
    --MENU--
    """)
        OpcionU = int(input("Seleccione una opcion: "))
        #Se usa match  para que sea más facil de leer y se llama a la clase correspondiente en base a la opcion
        match OpcionU:
            case 1: 
                print("--Se llama a la funcion para detectar mutaciones--")
                ADNU=Detector(matriz)
                TipoM = ADNU.detectar_mutantes()
                if TipoM:
                    print(f"Se detectó una {TipoM} en el ADN.")
                else:
                    print("No se detectaron mutaciones en el ADN.")
                
            case 2: 
                print("--Se llama a la funcion para mutar el ADN--")
                
            case 3: 
                print("--Se llama a la funcion para sanar mutaciones--")
               
            case 4: 
                print("--Se imprime el ADN ingresado--")
                print(matriz)
menu()
