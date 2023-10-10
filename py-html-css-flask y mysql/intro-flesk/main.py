'''FLASK'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

@app.route('/post/<post_id>')
def lala(post_id):
    return 'El ID del post es: ' + post_id

@app.route('/lele')
def lele():
    return 'lele'