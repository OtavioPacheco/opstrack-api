from main import app


def test_inicio():
    resposta = app.test_client().get("/")

    assert resposta.status_code == 200
    assert resposta.get_json() == {
        "Servico": "OpsTrackAPI",
        "Status": "ONLINE"
    }


def test_help():
    resposta = app.test_client().get("/help")

    assert resposta.status_code == 200
    assert resposta.get_data(as_text=True) == (
        "Pagina destinada a ajuda do user"
    )


def test_users():
    resposta = app.test_client().get("/users")

    assert resposta.status_code == 200
    assert resposta.get_json() == [
        {"email": "t@gmail.com", "nome": "tavi"},
        {"email": "a@gmail.com", "nome": "ana"}
    ]


def test_sobre():
    resposta = app.test_client().get("/sobre")

    assert resposta.status_code == 200
    assert resposta.get_data(as_text=True) == (
        "Projeto de exemplo, aula entrega continua"
    )


def test_equipe():
    resposta = app.test_client().get("/equipe")

    assert resposta.status_code == 200
    assert resposta.get_json() == [
        {"emailProfissional": "t@indaiatuba.sp.gov.br", "nome": "Paulo"},
        {"emailProfissional": "a@indaiatuba.sp.gov.br", "nome": "Ana"}
    ]
