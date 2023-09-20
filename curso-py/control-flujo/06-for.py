buscar = 5
for numero in range(1, 6):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break
else:
    print('el valor no se encontró')

for char in "Ultimate Python":
    if char == "m":
        print(char.upper(), " - ", "valor encontrado")
