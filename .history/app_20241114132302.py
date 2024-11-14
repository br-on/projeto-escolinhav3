from flask import Flask

app = Flask(__name__)

#rotas
@app.route("/") 
def homepage():
    return "meu site no flask"