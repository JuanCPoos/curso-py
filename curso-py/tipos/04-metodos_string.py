animal = "  chanCHito feliz  "
print(animal.upper())
# - metodo upper(), función que se encuentra dentro de un objeto
print(animal.lower())
print(animal.capitalize())  # 1er caracter del string y convierte en mayúscula
# convierte cada primer letra de cada palabra en mayúsucula y el resto en minúscula
print(animal.title())
print(animal.strip())  # -elimina espacios a la derecha e izquierda.

# exclusivo método strip()
print(animal.lstrip())
print(animal.rstrip())

# """podemos concatenar métodos"""
print(animal.strip().capitalize())

"""# -método find() busca el índice donde se encuentra la cadena de caracteres
pasada como argumento"""
print(animal.find("CH"))
print(animal.find("ch"))

# -método replace() reemplazar - recibe dos argumentos. Cad de caracteres y el valor por reemplazar
print(animal.replace("nCH", "j"))

# -busca si el caracter o cadena se encuentra en la variable. Devuelve Boolean
print("nCH" in animal)
print("nCH" not in animal)
