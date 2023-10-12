'''instrucciones schema'''
instructions = [
    'SET FOREIGN_KEY_CHECKS=0',
    'DROP TABLE IF EXISTS todo',
    'DROP TABLE IF EXISTS user',
    'SET FOREIGN_KEY_CHECKS=1',
    '''
    CREATE TABLE user(
        id INT PRIMARY KEY AUTO_INCREMENT,
        username VARCHAR(50) UNIQUE NOT NULL, 
        password VARCHAR(50) NOT NULL
    )
    ''',
    '''
        CREATE TABLE todo(
            id INT PRIMARY KEY AUTO_INCREMENT,
            created_by INT NOT NULL,
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            description TEXT NOT NULL, 
            completed BOOLEAN NOT NULL,
            FOREIGN KEY (created_by) REFERENCES user (id)            
        )
    '''
]

'''Lista de instrucciones SQL que se utilizan para definir y configurar las tablas de una base de datos:

'SET FOREIGN_KEY_CHECKS=0': Esta instrucción deshabilita temporalmente la verificación de claves foráneas en la base de datos. Esto permite realizar operaciones que involucran tablas relacionadas sin preocuparse por las restricciones de clave foránea. Por ejemplo, se utiliza antes de eliminar tablas para evitar errores relacionados con las restricciones de clave foránea.

'DROP TABLE IF EXISTS todo': Esta instrucción elimina la tabla llamada "todo" si existe. La cláusula IF EXISTS evita errores si la tabla no existe en la base de datos.

'DROP TABLE IF EXISTS user': Similar a la instrucción anterior, esta elimina la tabla "user" si existe.

'SET FOREIGN_KEY_CHECKS=1': Esta instrucción habilita nuevamente la verificación de claves foráneas en la base de datos después de haber deshabilitado esta verificación al comienzo del script.

Definición de la tabla "user":

id: Un campo de tipo INT que actúa como clave primaria y se autoincrementa.
username: Un campo de tipo VARCHAR que almacena el nombre de usuario, debe ser único y no nulo.
password: Un campo de tipo VARCHAR que almacena la contraseña del usuario y no puede ser nulo.
Definición de la tabla "todo":

id: Un campo de tipo INT que actúa como clave primaria y se autoincrementa.
created_by: Un campo de tipo INT que almacena el ID del usuario que creó la tarea.
created_at: Un campo de tipo TIMESTAMP que almacena la fecha y hora de creación de la tarea, con un valor predeterminado que es la hora actual.
description: Un campo de tipo TEXT que almacena la descripción de la tarea y no puede ser nulo.
completed: Un campo de tipo BOOLEAN que almacena un valor booleano para indicar si la tarea está completada o no.
FOREIGN KEY (created_by) REFERENCES user (id): Esta cláusula establece una restricción de clave foránea que relaciona el campo "created_by" de la tabla "todo" con el campo "id" de la tabla "user". Esto garantiza que cada tarea esté asociada a un usuario válido.
Estas instrucciones SQL son típicas en un script de configuración de base de datos. Se utilizan para crear las tablas necesarias y configurar las restricciones de clave foránea para un sistema de gestión de tareas (to-do list) que involucra usuarios y tareas.'''
