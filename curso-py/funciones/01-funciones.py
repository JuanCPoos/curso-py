def hola(nombre, apellido="porDefecto"):
    print('Hola mundo')
    print(f"Bienvenido: {nombre} {apellido}")     # f -> string formateado


# hola("Kevin", "comoArggs")
# hola("Chanchito")

# de esta forma podemos intercambiar la posición de los argumentos pero se van a asignar # igualmente a sus respectivos parámetros
hola(apellido="Schurmann", nombre="Kevin")
