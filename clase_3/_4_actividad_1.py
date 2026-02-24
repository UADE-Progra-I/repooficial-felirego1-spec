# ******************************************
# Actividad 1
# Listas y Metodos
# ******************************************

"""
Sugerencia:
dentro de la carpeta "codigo_estudiantes" crear un archivo python,
copiar y pegar alli estas consignas y trabajar en ese archivo
"""

# Datos para comenzar
estudiantes_header = ["id_estudiante", "nombre", "apellido", "email"]

estudiantes_datos = [
    ["Thiago", "Almada"],
    ["Agostina", "Hein"],
    ["Leandro", "Bolmaro"],
    ["Valentina", "Raposo"],
]

# 1
# Agregar emails ficticios usando append()
# Ejemplo: para Thiago Almada → [1, "Thiago", "Almada", "talmada@mail.com"].
estudiantes_datos[0].append("talmada@mail.com")
estudiantes_datos[1].append("ahein@mail.com")
estudiantes_datos[2].append("lbolmaro@mail.com")
estudiantes_datos[3].append("vraposo@mai.com")
#print(estudiantes_datos)
# 2
# Agregar los ids faltantes usando insert()
estudiantes_datos[0].insert(0,1)
estudiantes_datos[1].insert(0,2)
estudiantes_datos[2].insert(0,3)
estudiantes_datos[3].insert(0,4)
#print(estudiantes_datos)
# 3
# Agregar un nuevo estudiante al final con append()
# Hacer que el apellido de este estudiante se repita
# Ejemplo: [5, "Diego", "Almada", "dalmada@gmail.com"]
estudiantes_datos.append([5,"Diego","Almada","dalmada@gmail.com"])
print(estudiantes_datos)


# 4
# Eliminar un estudiante por apellido usando remove()
"""apellido_a_eliminar="Bolmaro"
for estudiante in estudiantes_datos: #recorre a cada estudiante de la lista estudiante datos
    if estudiante[2]==apellido_a_eliminar: #agarra la seccion apellidos
        estudiantes_datos.remove(estudiante)
        break
print(estudiantes_datos)"""


# 5
# Quitar el último estudiante usando pop() y mostrar qué estudiante fue eliminado.
"""estudiante_eliminado=estudiantes_datos.pop()
print(estudiante_eliminado)"""

# 6
# Buscar la posición (índice) de un apellido con index().
apellido_buscado="Bolmaro"
posicion=0
for estudiante in estudiantes_datos:
    if estudiante[2]==apellido_buscado:
        print (f"el apellido {apellido_buscado} se encuentra en la posicion {posicion}")
    else:
        posicion+=1
    
    


# 7
# Contar cuántos estudiantes tienen el mismo apellido con count() (simular apellidos repetidos agregando uno igual).
# Clue 1: generar una lista solo con apellidos
# Clue 2: investigar como implementarlo con listas por comprension
estudiante_apellidos= [estudiante[2] for estudiante in estudiantes_datos] #creo una lista solo con apellidos
print(estudiante_apellidos)
cantidad_de_almada=estudiante_apellidos.count("Almada") #cuento dentro de la lista estudiante apellido cuantos almada hay
print(cantidad_de_almada)

# 8
# Ordenar alfabéticamente los estudiantes por nombre
# Clue 1: Pueden usar sort pero deben combinarlo con funcion lambda
estudiantes_datos.sort(key=lambda x:x[1]) #combina funcion lambda con sort para ordenar de mayor a menor, x es cada lista de estudiante
print(estudiantes_datos)
# Clue 2: Pueden usar el método "Bubble Sort"

# NOTA:
# Si usan IA, debe ser con "pensamiento crítico"
