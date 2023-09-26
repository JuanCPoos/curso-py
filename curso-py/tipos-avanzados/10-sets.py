# set significa grupo o conjunto
# colección de datos que no se puede repetir (duplicados)
primer = {1, 1, 1, 2, 2, 3, 4, 4}
'''print(primer)
primer.add(6)
print(primer)
primer.remove(1)
print(primer)'''

segundo = [3, 4, 5]  # paréntesis cuadrados crea una lista
print("Lista: ", segundo)
segundo = set(segundo)
print("Set: ", segundo)

# operador de unión
print("Unificación: ", primer | segundo)

# operador de intersección - devuelve los elementos que se encuentren en ambas listas
print("Intersección: ", primer & segundo)

# diferencia entre dos sets - los datos del conjunto inzquierdo quitando aquellos elementos que se encuentran también en el conjunto dos.
print("Diferencia: ", primer - segundo)

# Diferencia simétrica - devuelve elementos que se encuentren entre uno y otro conjunto pero que no se encuentren en los dos.
# tecla especial Alt + 94 para el símbolo Acento circunflejo.
print("Diferencia simétrica: ", primer ^ segundo)
