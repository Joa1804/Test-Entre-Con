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

if __name__ == "__main__":
    app.run(debug=True)
