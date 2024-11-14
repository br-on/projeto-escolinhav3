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
