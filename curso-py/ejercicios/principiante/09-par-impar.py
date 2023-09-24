numero_usuario = input("Ingrese una lista de número: ")


def par_impar(parametro):
    if numero_usuario.lower() != 'salir' and int(numero_usuario) % 2 == 0:
        print(f"El número {numero_usuario} es par")
    elif numero_usuario.lower() != 'salir' and int(numero_usuario) % 2 == 1:
        print(f"El número {numero_usuario} es impar")


par_impar(numero_usuario)
