def numeros_pares(numeros):
    """Función que regresa una lista con los números pares de un conjunto dado."""
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    print(pares)
    return suma_pares(pares)


def suma_pares(pares):
    """Sumar todos los elementos pares de la lista y retornar su valor total."""
    suma = 0
    for par in pares:
        suma += par
    return suma


try:
    '''Código que podría generar una excepción'''
    limite_inferior = int(input('Ingrese el limite inferior del rango: '))
    if limite_inferior != "salir":
        print(f"Número ingresado: {limite_inferior}")
        limite_superior = int(input("Ingrese el limite superior del rango:"))
        if limite_superior != "salir":
            print(f"Número ingresado: {limite_superior}")
            numeros = list(range(limite_inferior, (limite_superior + 1)))
            print(numeros)
            print(
                f"La suma de los números pares entre {limite_inferior} y {limite_superior} es: {numeros_pares(numeros)}")
except Exception as e:
    # except Exception as e: # Si se quiere capturar cualquier tipo de error.
    print(f"Se produjo la excepción {e}")
else:
    print("Operación exitosa")
    # else: # Se ejecuta si no hubo errores en try y finally está presente.
