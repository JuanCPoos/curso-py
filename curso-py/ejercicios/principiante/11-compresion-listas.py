'''Imagina que estás creando un programa para gestionar una lista de usuarios. Cada usuario tiene un ID único, un nombre y una edad'''


usuario = [[10, "Juan", 33], [12, "Pedro", 28],
           [16, "Elena", 29], [14, "Melina", 33]]
print(usuario)


def agregar_usuario(id, nombre, edad):
    usuario.append([id, nombre, edad])


id = input('Ingrese el ID del nuevo usuario: ')
nombre = input('Ingrese el Nombre del nuevo usuario: ')
edad = input('Ingrese la edad del nuevo usuario: ')

usuarioOrdenados = sorted(usuario)  # ordena por el primer elemento de usuario
print(f"Ordenados por ID: {usuarioOrdenados}")
agregar_usuario(id, nombre, edad)
# print("Usuario ordenado por id:", usuarioOrdenados)
usuario.sort(key=lambda el: el[2])
print(f"Ordenados por edad: {usuario}")
