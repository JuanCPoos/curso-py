mascotas = ["Wolfgang", "Pelusa", "Pulga", "Copito"]

print(mascotas[2])
# indice de la izq, es dónde comienzo y el de la derecha hasta donde llegó
print(mascotas[2:])
# indica que toma el primer elemento y lo salta, toma el segundo y lo salta y muestra el 2
print(mascotas[::2])

numeros = list(range(21))
print(numeros[1::2])  # mostrará núm impares
print(numeros[::2])  # mostrará numeros pares
