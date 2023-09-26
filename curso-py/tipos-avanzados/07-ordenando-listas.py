# lista de prueba
numeros = [2, 4, 1, 45, 75, 22]

# sort() ordenamos la lista
numeros.sort()
print(numeros)

# sorted devuelve una nueva lista con los elementos ordenados. No modifica el original
ordenDos = sorted(numeros)
print(ordenDos)

# sort() ordenamos la lista al revés
numeros.sort(reverse=True)
print(numeros)

# lista usuarios que contienen otro listado de elementos con "id" y "nombre"
usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]
usuarios.sort()
print(usuarios)

# Ordenar por nombre en vez del id (primer elemento dentro de cada sublista). Usando key la cual La función key permite personalizar el criterio de ordenamiento de la lista.

usuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5]]

'''
def ordena(elemento):
    return elemento[1]

usuarios.sort(key=ordena)
'''

# Ordenamiento con el uso de expresiones lambda
# usuarios.sort(key=lambda parametro:valorRetorno)
usuarios.sort(key=lambda el: el[1])

print(usuarios)
