# estructura de un dicconario => variable = {"str" : valor cualquiera}
punto = {"x": 25, "y": 50}

print(punto["x"])
print(punto["y"])
punto["z"] = 10
print(punto["z"])
print(punto)

if "valor" in punto:
    print(punto["z"])

# método get para extrar el contenido del str del diccionario punto
print(punto.get("x"))
print(punto.get("alal"))
# si no ecuentra el str por defecto mostrar el valor a la derecha
print(punto.get("alal", 97))
print(punto.get("alal", "no encontrado"))

del punto["z"]  # eliminamos el valor asociado a la llave "z"
print(punto)

del (punto["y"])  # eliminamos la llave "y"
print(punto)

# Formas de mostrar los elementos de las llaves
puntoUno = {"Elena": 35, "Claudio": 18, "Anibal": 50}
for valor in puntoUno:
    print(valor, puntoUno[valor])

for valor in puntoUno.items():
    print(valor)

# desempaquetado
for llave, valor in puntoUno.items():
    print(llave, valor)


usuarios = [
    {"id": 1, "nombre": "Juan"},
    {"id": 2, "nombre": "Poos"},
    {"id": 3, "nombre": "Felipe"},
    {"id": 4, "nombre": "Paula"},
]

for usuario in usuarios:
    print(usuario['nombre'])
