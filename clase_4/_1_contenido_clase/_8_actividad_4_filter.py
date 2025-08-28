# *********************************************************************
# HACER UNA COPIA DE ESTE ARCHIVO A LA CARPETA
# CODIGO_ESTUDIANTES
# NO SOBRESCRIBIR ESTE ARCHIVO PARA EVITAR CONFLICTOS DE SINCRONIZACION
# *********************************************************************


# ---------------------------------------------------------------------
#  Ejercicio 1 - Limpiar inscripciones: quedarse solo con e-mails válidos
# ---------------------------------------------------------------------
"""
A partir de una lista de emails, se solicita filtrar aquellos que tengan un formato válido,
y con ellos retornar una nueva lista.


Finalmente, se sugiere normalizar la lista resultante, de manera que no tengan espacios en blanco
y todos sus caracteres se encuentren en minúcula.

Criterio simple: es str, contiene @ y .

Clue: correr el siguiente 
nombre = "ana"
cell = 1156568585
print(f"Es nombre una instancia de str?: ", isinstance(nombre, str))
print(f"Es cell una instancia de str?: ", isinstance(cell, str))

"""
estudiantes_datos = [
    ["Thiago", "Almada", 19, 8, "talmada@hotmail.com"],
    ["Agostina", "Hein", 25, 7, "ahein@hotmail.com"],
    ["Leandro", "Bolmaro", 22, 6.5, "lbolmaro.com"],
    ["Valentina", "Raposo", 24, 8.5, "vraposo@hotmail.com"],
]


mails_validos = [estudiante[4] for estudiante in estudiantes_datos if  isinstance(estudiante[4],str) and estudiante[4].endswith("@hotmail.com")]
#lo que hago en mails validos es decir que me filtre todo aquello que no es una cadena y tambien que me filtre todo aquel mail que no este terminado en @hotmail.com
print(mails_validos)
