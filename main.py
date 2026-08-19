from flask import Flask
app = Flask(__name__)
@app.route("/")
def projetoOtavio():
   return {"Servico": "OpsTrackAPI", "Status": "ONLINE"}

@app.route("/help")
def help():
    return "Tela de Ajuda"

if __name__ == "__main__":
   app.run(debug=True)