saludo = "Hola global"


def saludar():
    global saludo  # globalizar la variable
    saludo = "Hola mundo"
    print(saludo)


def saludaChanchito():
    saludo = "Hola Chanchito"


saludar()
print(saludo)
