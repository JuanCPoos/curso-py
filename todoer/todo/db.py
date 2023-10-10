'''base de datos'''
import mysql.connector

import click  # para ejecutar comandos en terminal
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions


def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            password=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE'],
        )
        g.c = g.db.cursor(dictionary=True)
    return g.db, g.c


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:  # si no se encuentra definido, no la hemos llamado, no hay que cerrarla
        db.close()


def init_db():
    """Crea las tablas del esquema."""
    db, c = get_db()

    for i in instructions:
        c.execute()

    db.commit()


@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')


def init_app(app):  # cada que se realice una petición a flask y devuelva el resultado llamara a close_db y cerrara la conexión
    app.teardown_appcontext(close_db)
