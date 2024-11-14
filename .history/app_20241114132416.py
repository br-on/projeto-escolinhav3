from flask import Flask

app = Flask(__name__)

#rotas
@app.route("/") #decorators
def homepage():
    return "meu site no flask"

if __name__ == "__main__":
    app.run()