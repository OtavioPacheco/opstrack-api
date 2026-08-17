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

if __name__ == "__main__":
   app.run(debug=True)