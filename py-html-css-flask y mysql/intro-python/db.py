'''db'''
import mysql.connector

midb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='coqui20alter',
    database='prueba'
)
cursor = midb.cursor()

cursor.execute('select * from Usuario')

resultado = cursor.fetchall()
print(resultado)
