from clases import  Detector, Mutador, Radiacion, Virus, Sanador

"""
Hay cosas por modificar a medida que se vayan haciendo el resto de clases
Se que la detector tiene que dar un booleano pero lo hice de esta forma así en un futuro
se si lo esta detectando bien, cuando me asegure de eso lo cambio a booleano para que solo de V o F
"""
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
    while True: 
        print("""
            --MENU--
            1. Detectar si hay mutaciones en el ADN
            2. Mutar ADN
            3. Sanar ADN
            4. Mostrar ADN ingresado
            --MENU--
            """)
        OpcionU = int(input("Seleccione una opción: "))
        
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
