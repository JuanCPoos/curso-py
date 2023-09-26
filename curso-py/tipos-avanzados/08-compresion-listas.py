listaUsuarios = [["Chanchito", 4], ["Felipe", 1], ["Pulga", 5], ["Enrico", 8]]
'''nombre = []
for usuario in usuarios:
    nombre.append(usuario[0])
print(nombre)'''


nombre = []
# nombre = [expresion for item in items] ->
# usuarios[0] indica qué elemento quiero extraer del item usuario de la lista usuarios
# -- map
# nombre = [usuario[0] for usuario in usuarios] # transformacion

# filtro --filter  para retonar elementos según condición dada
# nombre = [usuario for usuario in usuarios if usuario[1] > 2] # filtro

# nombre = [usuario[0] for usuario in usuarios if usuario[1] > 2]  # transformar y filtrar - LISTA DE COMPRENSIÓN

'''# lambda -> función anómima. recibe como argumento itemUsuario y quiero que me retorne itemsUsuario[0], osea return primer elemento de la sublista itemsUsuario.
nombres = list(map(lambda itemsUsuario: itemsUsuario[0], listaUsuarios))'''
# nombres será una lista que contiene los primeros elementos (usuario[0]) de cada objeto usuario en la lista usuarios.

nombres = list(filter(lambda usuario: usuario[1] > 2, listaUsuarios))

print(nombres)
