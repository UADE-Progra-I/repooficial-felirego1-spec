# ******************************************
# Actividad 2
# Listas por comprension
# ******************************************

"""
Ejercicio 1: Números impares elevados al cubo
Dada una lista de números del 1 al 10, generar una nueva lista que contenga
los cubos de los números impares."""

numeros = list(range(1, 11))
cubos_impares = [num**3 for num in numeros if num %2 !=0]  # completar
print("Cubos de impares:", cubos_impares)
# Resultado esperado: [1, 27, 125, 343, 729]


"""
Ejercicio 2: Filtrar palabras cortas
Dada una lista de palabras, obtener otra lista con solo aquellas que tengan
 4 o menos caracteres.
"""

palabras = ["sol", "luna", "estrella", "mar", "cielo", "ave"]
palabras_cortas = [palabra for palabra in palabras if len(palabra)<=4 ]  # completar
print("Palabras cortas:", palabras_cortas)
# Resultado esperado: ["sol", "luna", "mar", "ave"]


"""
Ejercicio 3: Clasificación de números
Dada una lista de enteros, crear una nueva lista que contenga la palabra "Positivo" si el número es mayor a 0, "Negativo" si es menor a 0, y "Cero" si es igual a 0.
"""

lista = [3, -1, 0, 7, -5, 2]
clasificacion = ["positivo" if numero>=0 else "negativo" for numero in lista]  # completar
print("Clasificación:", clasificacion)
# Resultado esperado: ["Positivo", "Negativo", "Cero", "Positivo", "Negativo", "Positivo"]
