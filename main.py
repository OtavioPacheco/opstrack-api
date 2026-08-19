from flask import Flask
app = Flask(__name__)
@app.route("/")
def projetoOtavio():
   return {"Servico": "OpsTrackAPI", "Status": "ONLINE"}

@app.route("/help")
def help():
    return "Tela de Ajuda"

@app.route("/usuarios")
def users():
    return {"nome": "Otavio", "email": "tavi123@gmail"}

@app.route("/sobre")
def sobre():
    return "Api direcionada aos usuarios"

@app.route("/equipe")
def equipe():
    return "Bento, Otavio, Gustavo, Davi, Cauan, Tiago"

if __name__ == "__main__":
   app.run(debug=True)