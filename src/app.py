from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Sistema de Gerenciamneto de Bliblioteca"

@app.route("/sobre")
def sobre():
    return "Sistema desenvolvido em Flask para estudo de CI/CD"

@app.route("/status")
def status():
    return {"status": "API online"}

@app.route("/livros")
def livros():
    return "Lista de livros cadastrados"

@app.route("/autores")
def autores():
    return "Lista de autores cadastrados"


if __name__ == "__main__":
    app.run(debug=True)
