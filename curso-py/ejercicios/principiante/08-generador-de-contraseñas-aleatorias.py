import random
import string


def generar_contrasena(longitud, may, min, num, simb):
    if caracteres_especiales == "may":
        letras = string.ascii_uppercase + string.digits  # A-Z+0-9
    elif caracteres_especiales == "min":
        letras = string.ascii_lowercase + string.digits   # a-z+0-9
    elif caracteres_especiales == "num":
        letras = string.ascii_lowercase + string.digits   # a-z+0-9
    elif caracteres_especiales == "simb":
        letras = string.ascii_lowercase + string.digits   # a-z+0-9
    else:
        # Todas las letras del alfabeto (A-Za-z) +
        letras = string.printable


long_contraseña = input('Especifique la longitud de la contraseña a crear')
# print(type(long_contraseña))
caracteres_especiales = input(
    'Para incluir caracteres especiales, indique: may, min, num y/o simb')

generar_contrasena(long_contraseña, may)
