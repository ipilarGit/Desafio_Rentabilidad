# Contexto

# Un emprendedor quiere crear una aplicación y necesita saber si es rentable,
# para ello, se le pide desarrollar los siguientes tres casos, estos problemas 
# son independientes el uno del otro por lo que puede desarrollarlos en 
# el orden que le parezca conveniente.

# 1. Crear un programa emprendedor1.py donde el usuario ingrese el precio de venta de
# un servicio, el número de usuarios suscritos y los gastos asociados. El programa,
# además, debe calcular y mostrar las utilidades de acuerdo a la siguiente función:
# utilidades = precio_venta * usuarios − gastos

import sys

argumentos=len(sys.argv)
if argumentos == 4:
    precio_venta_servicio = int(str(sys.argv[1]))
    usuarios_suscritos = int(str(sys.argv[2]))
    gastos_asociados = int(str(sys.argv[3]))
    utilidades = (precio_venta_servicio * usuarios_suscritos) - gastos_asociados 
    print ("La utilidades del emprendimiento son: {}".format(utilidades))
else:
    print("ERROR: Intodujo (1) ó (2) ó (3) argumentos.")
    print("SOLUCION: Intoduce los argumentos correctamente.")
    print("\nPara determinar la utilidades del emprendimiento, escribe por consola:")
    print("$ python emprendedor1.py precio_venta_servicio usuarios_suscritos gastos_asociados")
