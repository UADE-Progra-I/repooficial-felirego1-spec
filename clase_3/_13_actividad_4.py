# Ejercicios: Cadenas de caracteres en Python
texto="programacion"
cadena= str(texto)

# Ejercicio 1: Extracción de caracteres
"""
Dada la cadena "programacion", mostrar:

El primer carácter.

El último carácter.
Los caracteres de la posición 2 a la 6.

Pista: usar índices y slicing (str[i:j]).
"""
primer_caracter=cadena[0]
ultimo_caracter=cadena[-1]
recortada=cadena[2:6]
print(primer_caracter)
print(ultimo_caracter)
print(recortada)
# Ejercicio 2: Normalización de texto

"""
Dada la cadena " Python Es GENIAL ", obtener:
El texto sin espacios al inicio y al final.
Todo en minúsculas.
Todo en mayúsculas.

Pista: usar strip(), lower(), upper().
"""
cadena1= " Python Es GENIAL "
cadena_sin_espacios=cadena1.strip() #elimina espacios solo al inicio y final
cadena_minuscula=cadena1.lower()
cadena_mayuscula=cadena1.upper()
print(cadena_sin_espacios)
print(cadena_mayuscula)
print(cadena_minuscula)
# Ejercicio 3: Reemplazo y conteo

"""
Dada la cadena "hola mundo hola python", realizar:

Reemplazar "hola" por "chau".
Contar cuántas veces aparece la letra "o".
Buscar la posición de la primera "m".

Pista: usar replace(), count(), find().
"""
cadena2="hola mundo hola python"
reemplazo_cadena= cadena2.replace("hola", "chau")
conteo_o= cadena2.count("o")
posicion_m= cadena2.find("m")
print(reemplazo_cadena)
print(conteo_o)
print(posicion_m)


# Ejercicio 4: Separar y unir palabras

"""
Dada la cadena "rojo,verde,azul,amarillo", 
generar una lista con las palabras y luego volver a unirlas separadas por un guion ("-").

Pista: usar split() y join().

"""

cadena3="rojo,verde,azul,amarillo"
lista_cadena3= cadena3.split(",") #convierto una cadena en una lista
print(lista_cadena3)
cadena_cambiada="-".join(lista_cadena3) #vuelvo a unir en una lista pero con guion en ves de coma
print(cadena_cambiada)

# Ejercicio 5: Validación de entradas

""" 
Pedir al usuario que ingrese un texto y verificar:

Si solo contiene letras (isalpha()).
Si solo contiene números (isnumeric()).
Si es alfanumérico (isalnum()).

Pista: usar un input() y luego aplicar los métodos.

"""
texto= input("ingrese un texto")
if texto.isalpha():
    print("el texto solo contiene letras")
if texto.isnumeric():
    print("el texto solo contiene numeros")
if texto.isalnum():
    print("el texto es alfanumerico")
