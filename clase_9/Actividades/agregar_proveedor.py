# --------------------------------------------------------
# Actividad manejo de excepciones
# --------------------------------------------------------

"""
El siguiente código consiste en una carga de proveedores a una lista de diccionarios
La función crear_proveedor(), recibe la variable proveedores,
solicita por consola y valida nombre e e-mail
Luego invoca a la función siguiente_id para que el id de inserción sea único

1. Cómo se podria mejorar usando manejo de excepciones?
2. Qué sucede si por alguna razón, la función siguiente_id no se puede invocar? Cómo mejorarían el código?
"""

# Importar librerías
import re

# Variable global
proveedores = []

# Patrones de validación
P_NOMBRE = r"^[A-Za-zÀ-ÿÑñ\s]{2,50}$"
P_EMAIL = r".+@.+\..+"


def main():
    crear_proveedor(proveedores)
    print(proveedores)

def siguiente_id(matriz):
    try:
        return (max([x["id"] for x in matriz]) + 1) if matriz else 1
    except (KeyError,TypeError, ValueError) as e:
        print(f"Error al calcular el siguiente ID: ´{e}")
        return 1 


def crear_proveedor(proveedores):

    # Solicitar y validar nombre
    while True:
        nombre = input("Ingrese el nombre del proveedor: ")
        if re.match(P_NOMBRE, nombre):
            break
        print("Error: Nombre invalido")

           # Solicitar y validar email
    while True:
        email = input("Ingrese el email del proveedor: ")
        if re.match(P_EMAIL, email):
            break
        print("Error: Email inválido")
    
    try:
        nuevo_id= siguiente_id(proveedores)
    except Exception as e:
        print(f"No se pudo generar un ID unico:{e}")
        nuevo_id= 1 

    proveedor = {
        "id": siguiente_id(proveedores),
        "nombre": nombre,
        "email": email
    }

    print("Proveedor agregado exitosamente.")
    proveedores.append(proveedor)



if __name__ == "__main__":
    main()