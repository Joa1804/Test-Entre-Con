from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/livros")
def livros():
    return render_template("livros.html")

@app.route("/autores")
def autores():
    return render_template("autores.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)