'''Calcular la nota final de un estudiante basada en tres notas parciales ponderadas.'''

'''calcularNota() toma tres argumentos que son las notas parciales se las multiplica
por su ponderación y se suman'''
def calcularNota(n1, n2, n3):
    resultado = (n1*0.3) + (n2*0.3) + (n3*0.4)
    return resultado

n1 = float(input('Ingrese la primer nota:'))
n2 = float(input('Ingrese la segunda nota:'))
n3 = float(input('Ingrese la tercera nota:'))

resultadoFinal = calcularNota(n1, n2, n3)

print(f'La nota final del estudiante es: {round(resultadoFinal, 2)}')