# views.py
from flask import Blueprint, render_template

# Cria um Blueprint para as views
views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/membros')
def membros():
    return render_template('membros.html')

@views.route('/pagamentos')
def pagamentos():
    return render_template('pagamentos.html')

@views.route('/eventos')
def pagamentos():
    return render_template('eventos.html')

@views.route('/perfil')
def pagamentos():
    return render_template('perfil.html')

