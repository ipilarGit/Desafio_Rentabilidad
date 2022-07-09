# 3. Crear el programa emprendedor3.py donde el usuario ingrese el precio, 
# el número de usuarios, los gastos y las utilidades del año anterior 
# (en ese orden), este último parámetro será optativo, si el usuario no 
# lo ingresa se asumirá 1000 dólares como base. El programa debe calcular 
# y mostrar la razón entre las utilidades actuales y las del año anterior,
# esto quiere decir, por ejemplo, que obtener un valor de dicha razón
# superior a 1 significa que las utilidades actuales fueron superiores a
# las anteriores. Su programa también debe mostrar las utilidades actuales,
# para calcular estas utilice la misma fórmula mostrada
# en el problema de emprendedor1.py

import sys

argumentos=len(sys.argv)

DOLAR = 716
if argumentos == 4:     
    utilidades_year_anterior = 1000 * DOLAR
    
if argumentos == 5:
    utilidades_year_anterior = int(str(sys.argv[4]))
    utilidades_year_anterior = utilidades_year_anterior * DOLAR

if (argumentos == 4 or argumentos == 5) :
    precio = int(str(sys.argv[1]))
    numero_usuarios = int(str(sys.argv[2]))
    gastos_asociados = int(str(sys.argv[3]))
    utilidades_actuales = (precio * numero_usuarios) - gastos_asociados
    razon_utilidades = (utilidades_actuales / utilidades_year_anterior)
    if razon_utilidades > 1 :
        print("\nLa razón entre las utilidades es de: {0:.2f}, lo que indica que las utilidades del año actual fueron superiores a las del año anterior.".format(razon_utilidades))
    elif razon_utilidades == 1:
        print("\nLa razón entre las utilidades es de: {0:.2f}, lo que indica que las utilidades del año actual y las del año anterior se mantuvieron.".format(razon_utilidades))
    else:
        print("\nLa razón entre las utilidades es de: {0:.2f}, lo que indica que las utilidades del año anterior fueron superiores a las del año actual.".format(razon_utilidades))
    print("Las utilidades del año anterior fueron: $ {}".format(utilidades_year_anterior))
    print("Las utilidades del año actual son     : $ {}".format(utilidades_actuales))
else:
    print("ERROR: Intodujo menos de (4) ó (5) argumentos.")
    print("SOLUCION: Intoduce los argumentos correctamente.")
    print("\nPara determinar la utilidades del emprendimiento, escribe por consola:")
    print("$ python emprendedor3.py precio numero_usuarios gastos_asociados [utilidades_año_anterior] ")


