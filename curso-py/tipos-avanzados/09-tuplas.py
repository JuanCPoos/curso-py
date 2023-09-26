# lista que no quiero modificar, paréntesis
listaNumeros = (1, 2, 3) + (4, 5, 6)
print(listaNumeros)

# lista transformada a tupla
punto = tuple([1, 2])
puntoUno = tuple(listaNumeros)
print(punto)
print(puntoUno)

menosNumeros = listaNumeros[:2]
print(menosNumeros)

primero, segundo, *otros = listaNumeros
print(primero, segundo, otros)

print("Transformación de la tupla a lista y modificación que no se debe")
listaNueva = list(puntoUno)
listaNueva[1] = 'Chanchito Feliz'
print(listaNueva)
