from random import randint

import csv
trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
todos_los_trabajadores=["Juan Perez", "Maria Garcia", "Carlos Lopez", "Ana Martinez", "Pedro Rodrigez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Franciscos Dias", "Elena Fernandez"]
consueldos=[]

def asignar_sueldos_aleatorios():
    for t in todos_los_trabajadores:
        consueldos.append(["nombre:",t,"sueldo",randint(200000,3500000),])
    print(consueldos)
    return consueldos  

def clasificar_sueldos():
    for i in consueldos:
        if i[3]<800000:
           print("Los sueldos menores de 800.000 son: ", i)
           sueldobase=i[3]
           descuentoafp=i[3]*0.07
           descuentosalud=i[3]*0.12
           sueldoliquido=sueldobase-descuentoafp-descuentosalud
           print(sueldoliquido)
           
        elif i[3]>=800000 and i[3]<2000000:
            print("Los sueldos entre 800.000 y 2.000.000 son:", i)
            sueldobase=i[3]
            descuentoafp=i[3]*0.07
            descuentosalud=i[3]*0.12
            sueldoliquido=sueldobase-descuentoafp-descuentosalud
            print(sueldoliquido)
            
        elif i[3]>=2000000:
            print("Los sueldos mayores a 2000000 son:", i)
            sueldobase=i[3]
            descuentoafp=i[3]*0.07
            descuentosalud=i[3]*0.12
            sueldoliquido=sueldobase-descuentoafp-descuentosalud
            print(sueldoliquido)
            

def imprimir_sueldos():
    nombre_archivo="Lista de sueldos.csv"
    with open(nombre_archivo,"w", newline="") as archivo_csv:
        escritor_csv=csv.writer(archivo_csv)
        for i in consueldos:
            escritor_csv.writerow(i)
        print("Guardado en:", nombre_archivo)
def salir():
    print("Gracias por usar el programa")
while True:
    print("1. Asignar sueldos")
    print("2. Clasificar sueldos")
    print("3. Imprimir lista")
    print("4. Salir")
    opcion=int(input(""))
        
    if opcion==1:
        persona=asignar_sueldos_aleatorios()

    elif opcion==2:
        clasificar_sueldos()
    elif opcion==3:
        imprimir_sueldos()
    elif opcion==4:
        salir()
        break
