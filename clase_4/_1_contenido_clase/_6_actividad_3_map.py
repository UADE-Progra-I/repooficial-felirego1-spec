# *********************************************************************
# HACER UNA COPIA DE ESTE ARCHIVO A LA CARPETA
# CODIGO_ESTUDIANTES
# NO SOBRESCRIBIR ESTE ARCHIVO PARA EVITAR CONFLICTOS DE SINCRONIZACION
# *********************************************************************


# ---------------------------------------------------------------------
#  Ejercicio 1 - Convertir temperaturas
# ---------------------------------------------------------------------
"""
Dada la lista de temperaturas en °C, obtené una nueva lista
con las temperaturas en °F, redondeadas a 1 decimal.

Clue: fórmula → F = C * 9/5 + 32 y usá round(valor, 1).
"""




# ---------------------------------------------------------------------
#  Ejercicio 2 - Promedio ponderado de notas
# ---------------------------------------------------------------------
"""
Dados dos listados paralelos con notas de parcial y final, 
calculá el promedio ponderado 0.4*parcial + 0.6*final para cada alumno. 
Redondeá a 1 decimal.
"""

notasparcial=[7,8,8,9]
notasfinal=[6,7,8,9]
notatotal=list(map(lambda x,y:round(x*0.4 + y*0.6,1), notasparcial, notasfinal)) #lo que me dice es que tengo 2 listas x e y y quiero sumarlas asi pero que sea redondea a 1 decimal.
print(notatotal) #el round en python es para redondear









# ---------------------------------------------------------------------
#  Ejercicio 3 - Normalizar los nombres y apellidos de los estudiantes
# ---------------------------------------------------------------------
"""
Se solicita normalizar los nombre y apellidos de los estudiantes, de manera
que todos sus caracteres sean en minúscula, salvo la primer letra.
"""

estudiantes=["felipe","facundo","lisandro","luciano"]
estudiantesmayus=list(map(lambda x : x.title(),estudiantes)) #el comando title se pone la primer letra en mayuscula
print(estudiantesmayus)