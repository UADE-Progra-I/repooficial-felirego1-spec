# *********************************************************************
# HACER UNA COPIA DE ESTE ARCHIVO A LA CARPETA
# CODIGO_ESTUDIANTES
# NO SOBRESCRIBIR ESTE ARCHIVO PARA EVITAR CONFLICTOS DE SINCRONIZACION
# *********************************************************************

# ---------------------------------------------------------------------
#  Ejercicio 1 - Ordenar una lista de listas
# ---------------------------------------------------------------------
"""
Declarar una lista de listas con una matriz de tu proyecto.
Luego generar una función que retorne la lista ordenada por alguna variable numérica.

Clue: usar función sorted combinada con lambda para ordenar ese arreglo
"""
estudiantes_datos = [
    ["Thiago", "Almada", 19],
    ["Agostina", "Hein", 25],
    ["Leandro", "Bolmaro", 22],
    ["Valentina", "Raposo", 24],
]
estudiantes_datos.sort() #si yo pongo esto asi me los ordena automaticamente por el primer dato que es el nombre que viene a ocupar la posicion 0
print(estudiantes_datos)

estudiantes_datos_ordenados = sorted(estudiantes_datos, key=lambda x: x[2]) #asi me los ordena por el 2do dato que es la edad de menor a mayor
print(estudiantes_datos_ordenados)
# ---------------------------------------------------------------------
#  Ejercicio 2 - Invertir el orden
# ---------------------------------------------------------------------
"""
Generar una función complementaria, que además de ordenar, 
lo haga de forma ascendente o descendente, según indique el usuario 
"""





