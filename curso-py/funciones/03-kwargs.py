def get_product(**datos):
    print(datos["id"], datos["name"])


get_product(id="23",  # id="id" -> nombre de argumento y parámetro
            name="iPhone",
            desc="Esto es un iphone")
