
def contarPalabras(parametro):
    # Divide la cadena de texto en palabras usando espacios en blanco como separadores
    palabras = parametro.split()
    # Las palabras quedan almacenadas en la variable "palabras"
    cantidad_palabras = len(palabras)
    #    cantidad_palabras almacena la cantidad de palabras usando la function len()
    return cantidad_palabras


cadena_args = input('Ingrese texto: ')
resultado = contarPalabras(cadena_args)
print(resultado)
