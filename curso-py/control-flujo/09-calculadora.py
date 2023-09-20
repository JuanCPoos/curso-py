print('Bienvenidos a la calculadora. \nPara salir escribe salir')
result = ""
while True:
    if not result:  # false - 0 - " " -
        result = input('Ingrese un número: ')
        if result.lower() == "salir":
            break
        result = int(result)
    op = input('Ingrese una operación, suma - multi - div - resta:')
    if (op.lower() == "salir"):
        break
    segundoNum = input('Ingrese otro número: ')
    if segundoNum.lower() == "salir":
        break
    segundoNum = int(segundoNum)
    if op.lower() == 'suma':
        result += segundoNum
    elif op.lower() == 'multi':
        result *= segundoNum
    elif op.lower() == 'div':
        result /= segundoNum
    elif op.lower() == 'resta':
        result -= segundoNum
    else:
        print('Operación no válida')
        break
    print(f"El resultado es: {result}")
