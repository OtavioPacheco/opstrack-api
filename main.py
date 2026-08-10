from flask import Flask
app = Flask(__name__)
@app.route("/")
def projetoOtavio():
   return {"Servico": "OpsTrackAPI", "Status": "ONLINE"}

if __name__ == "__main__":
   app.run(debug=True)