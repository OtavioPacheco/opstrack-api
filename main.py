from flask import Flask
app = Flask(__name__)
@app.route("/")
def projetoOtavio():
   return {"Servico": "OpsTrackAPI", "Status": "ONLINE"}
#teste
@app.route("/help")
def help():
   return "Pagina destinada a ajuda do user"

@app.route("/users")
def users():
   return [{"email": "t@gmail.com", "nome": "tavi"},
            {"email": "a@gmail.com", "nome": "ana"}]

@app.route("/sobre")
def sobre():
   return "Projeto de exemplo, aula entrega continua"

@app.route("/equipe")
def equipe():
   return [{"emailProfissional": "t@indaiatuba.sp.gov.br", "nome": "Paulo"},
            {"emailProfissional": "a@indaiatuba.sp.gov.br", "nome": "Ana"}]

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