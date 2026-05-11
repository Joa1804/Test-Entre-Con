from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
        return Sistema de Gestão de Biblioteca

@app.route("/sobre)
def sobre():
    return "Sistema desenvolvido em Flask para estudo de CI/CD"

@app.route("/status)
def status():
    return {"status": "ok"}

@app.route("/livros)
def livros():
    return "Lista de livros cadastrados"

@app.route("/autores")
def autores():
    return "Lista de autores cadastrados"

@app.route("/contato")
def contato():
    return "Página de contato do sistema"

@app.route("/cadastro-livro")
def cadastro_livro():
    return "Página de cadastro de livros"

if __name__ == "__main__":
    app.run(debug=True)
