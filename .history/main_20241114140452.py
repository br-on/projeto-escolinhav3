# app.py
from flask import Flask
from views import views  # Importa o Blueprint

app = Flask(__name__)

# Registra o Blueprint das views
app.register_blueprint(views)

if __name__ == '__main__':
    app.run(debug=True)
