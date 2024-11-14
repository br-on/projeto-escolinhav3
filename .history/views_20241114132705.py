from app import app

# rotas
@app.route("/") #decorators
def homepage():
    return "meu site no flask agora"