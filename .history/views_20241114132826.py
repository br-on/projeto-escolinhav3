from main import app

# rotas
@app.route("/") #decorators
def homepage():
    return "meu site no flask agora"

@app.route("/blog") #decorators
def blog():
    return "este é o blog"