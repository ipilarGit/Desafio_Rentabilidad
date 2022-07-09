# 2. Considere ahora el siguiente caso: Se tienen tres tipos de usuarios,
# los usuarios normales que pagan una cantidad estándar por suscripción, 
# los usuarios premium que pagan el doble de los usuarios normales y 
# los usuarios en período de prueba que no pagan nada.

# Genere un programa llamado emprendedor2.py que reciba la cantidad de usuarios
# normales, la cantidad de usuarios premium, la cantidad de usuarios en período 
# de prueba, el valor estándar del servicio y los gastos asociados y muestre las 
# utilidades de forma similar al caso de emprendedor1.py, es decir, multiplicando
# el precio de venta por el tipo de usuario correspondiente y restando los gastos

import sys

argumentos=len(sys.argv)
if argumentos == 6:
    usuarios_normales = int(str(sys.argv[1]))
    usuarios_premium = int(str(sys.argv[2]))
    usuarios_periodo_de_prueba = int(str(sys.argv[3]))
    suscripcion_estandar = int(str(sys.argv[4]))
    gastos_asociados = int(str(sys.argv[5]))
    suscripcion_usuarios_premium = 2 * suscripcion_estandar
    suscripcion_periodo_de_prueba = 0
    utilidades = ((suscripcion_estandar * usuarios_normales) + (suscripcion_usuarios_premium * usuarios_premium) + (suscripcion_periodo_de_prueba * usuarios_periodo_de_prueba)) - gastos_asociados
    print ("Las utilidades del emprendimento son: $ {}".format(utilidades))
else:
    print("ERROR: Intodujo menos de (5) argumentos.")
    print("SOLUCION: Intoduce los argumentos correctamente.")
    print("\nPara determinar la utilidades del emprendimiento, escribe por consola:")
    print("$ python emprendedor2.py cantidad_usuarios_normales cantidad_usuarios_premium cantidad_usuarios_periodo_prueba precio_suscripcion_estandar gastos_asociados")
