from main import app
from flask import render_template

# rotas
@app.route("/") #decorators
def homepage():
    return "meu site no flask agora"

@app.route("/blog") #decorators
def blog():
    return "este é o blog"