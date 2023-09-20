# - and, or, not

# gas = True
# encendido = True
# mensaje = "Arrancar" if gas and encendido else "No puedes arrancar"


# gas = False
# encendido = True
# mensaje = "Arrancar" if gas or encendido else "No puedes arrancar"

# gas = True
# encendido = False
# if not gas or encendido:
#     mensaje = "Arrancar"
# else:
#     mensaje = "No puedes arrancar"


gas = False
encendido = True
edad = 16

# if not gas and (encendido and edad > 17):
#     print("puede avanzara")
# else:
#     print("no puede avanzar")


# - OPERADORES DE CORTOCIRCUITO

if not gas or (encendido and edad > 17):
    print("puede avanzara")
else:
    print("no puede avanzar")

# print(mensaje)
