mascotas = ["wolfgang",
            "pelusa",
            "pulga",
            "wolfgang",
            "felipe",
            "pulga",
            "chanchito feliz"
            ]
# metodo insert(indice, "elemento") => insertamos un nuevo elemento
mascotas.insert(1, "melvin")
print(mascotas)

# metodo append() => insertamos un nuevo elemento al final
mascotas.append("chanchito triste")
print(mascotas)

# metodo remove() => removemos/eliminamos la primer ocurrencia del elemento dado
mascotas.remove("pulga")
print(mascotas)

# metodo pop() => removemos/eliminamos el último elemento del listado
mascotas.pop()
print(mascotas)

# metodo pop(indice) => removemos/eliminamos el indicado en el indice
mascotas.pop(1)
print(mascotas)

# del -> elimina elementos dentro de un arreglo dado por el indice indicado
del mascotas[0]
print(mascotas)
# cantidad de elementos del listado mascotas
print(len(mascotas))

# metodo clear() limpia el arreglo completo
mascotas.clear()
print(mascotas)
