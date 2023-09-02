# Ejemplo de diccionario
canciones = {
    10:"Si estuviesemos juntos",
    20:"Cuento",
    30:"Otra noche en miami",
    40:"Como antes",
    50:"Agosto"
}
print(len(canciones))
print(canciones.keys())
print(canciones.values())

print(type(canciones))



""" contactos = {}

while True:
    nombre = input("Ingresa el nombre: ")

    if nombre.strip() == "":
        break

    telefono = input("Ingresa el telefono: ")
    nueva_clave = max(contactos.keys(), default=0) + 1
    contactos[nueva_clave]=(nombre, telefono)

print(contactos) """

""" print(contactos[2])  """#Esta manera está bien

#Forma recomendable y la mejor manera de poder ver la posicion del diccinario que desea
# | = pipe = tubo en python es un operador que su funcion es juntar los diccionarios en un solo conjunto
# en un conjunto solo se pueden tener elementos inmutables, los conjuntos no garantizan el orden 
# de los elementos

#

# print(contactos.get(2, "NO EXISTE"))

# una operación de conjuntos siempre tiene como resultado un nuevo conjunto

# conjunto_uno = {"Hugo", "Paco", "Luis"}
#conjunto_dos = {"Britni", "Llojan", "Luis"}

# Diferencia
# print(conjunto_uno - conjunto_dos)

# Diferenia simétrica
# print(conjunto_uno ^ conjunto_dos)

# import random
# valores = [random.randrange(1,6) for valor in range(100)]
# print(valores)

# diferentes = set(valores)
# print()
# print(diferentes)

# First In First Out - Primero en llegar es el primero en salir

# cola = list()

# for cantidad in range(5):
#    nuevo = input("Nombre del recién llegado: ")
#    cola.append(nuevo)
# print(f"Se agregaron {(len(cola))} elementos")
# print("Procedemos a retirarlos de la cola: ")
# while cola:
#    cola.pop(0)
#pass 

# Last In First Out - Apilar objetos - Último en llegar es el primero en salir 