estudiantes_header = ["id_estudiante", "nombre", "apellido", "email"]

estudiantes_datos1 = ["Thiago", "Almada"]
estudiantes_datos2=["Agostina", "Hein"]
estudiantes_datos3=["Leandro", "Bolmaro"]
estudiantes_datos4=["Valentina", "Raposo"]
estudiantes_datosf=[estudiantes_datos1,estudiantes_datos2,estudiantes_datos3,estudiantes_datos4]
print(estudiantes_datosf)

# 1
# Agregar emails ficticios usando append() #append te agrega al final de la lista el valor
# Ejemplo: para Thiago Almada → [1, "Thiago", "Almada", "talmada@mail.com"].
estudiantes_datos1.append("talmada@gmail.com")
estudiantes_datos2.append("ahein@gmail.com")
estudiantes_datos3.append("lbolmaro@gmail.com")
estudiantes_datos4.append("vraposo@gmail.com")
print(estudiantes_datosf)

# 2
# Agregar los ids faltantes usando insert() #en la posicion 0 se agrega el numero 1000 y se desplaza el valor al siguiente.
estudiantes_datos1.insert(0,1001)
estudiantes_datos2.insert(0,1002)
estudiantes_datos3.insert(0,1003)
estudiantes_datos4.insert(0,1004)
print(estudiantes_datosf)

# 3
# Agregar un nuevo estudiante al final con append()
# Hacer que el apellido de este estudiante se repita
# Ejemplo: [5, "Diego", "Almada", "dalmada@gmail.com"]

estudiantes_datos5=[1005,"Diego","Almada", "dalmada@gmai.com"]
estudiantes_datosf.append(estudiantes_datos5)
print(estudiantes_datosf)
# 4
# Eliminar un estudiante por apellido usando remove()
#eliminar=input("ingrese un apellido que quiera eliminar")
#while eliminar!= "Hein","Bolmaro","Raposo":
   #eliminar=input("error,re-ingrese un valor correcto de apellido")
      



for estudiante in estudiantes_datosf:
    if "Almada" in estudiante:
        estudiantes_datosf.remove(estudiante)
        break  # Salimos del bucle después de eliminar Almada para que no me siga eliminando si hay gente almada

print(estudiantes_datosf)


# 5
# Quitar el último estudiante usando pop() y mostrar qué estudiante fue eliminado.
elementopop=estudiantes_datosf.pop() #elimina el ultimo elemento
print(estudiantes_datosf)
print(elementopop)#el elemento que se elimino


# 6
# Buscar la posición (índice) de un apellido con index().



# 7
# Contar cuántos estudiantes tienen el mismo apellido con count() (simular apellidos repetidos agregando uno igual).
# Clue 1: generar una lista solo con apellidos
# Clue 2: investigar como implementarlo con listas por comprension

estudiantes_datos1 = ["Thiago", "Almada"]
estudiantes_datos2=["Agostina", "Hein"]
estudiantes_datos3=["Leandro", "Bolmaro"]
estudiantes_datos4=["Valentina", "Raposo"]
estudiantes_datosf=[estudiantes_datos1,estudiantes_datos2,estudiantes_datos3,estudiantes_datos4]
estudiantes_datos5=["Diego","Almada"]
estudiantes_datos6=["Rodrigo","Bolmaro"]
estudiantes_datosf.append(estudiantes_datos5)
estudiantes_datosf.append(estudiantes_datos6)

apellidos= [estudiante [1] for estudiante in estudiantes_datosf] #saco de la lista los valores "apellidos" que se encuentran en la posicion 1 
print(apellidos)
cantidad_almada=apellidos.count("Almada")
print(cantidad_almada)

# 8
# Ordenar alfabéticamente los estudiantes por nombre
# Clue 1: Pueden usar sort pero deben combinarlo con funcion lambda
# Clue 2: Pueden usar el método "Bubble Sort"
estudiantes_datosf.sort(key=lambda estudiante: estudiante[0]) #ordena la lista de acuerdo a los nombres que se encuentran en la posicion 0
#sort ordena de mayor a menor.
for estudiante in estudiantes_datosf:
    print(estudiante)
# NOTA:
# Si usan IA, debe ser con "pensamiento crítico"
#si lo quiero hacer por apellido.
estudiantes_datosf.sort(key=lambda estudiante:estudiante[1]) #el sort key lambda indica que se ordena de manera alfabetica.
for estudiante in estudiantes_datosf:
    print(estudiante)
