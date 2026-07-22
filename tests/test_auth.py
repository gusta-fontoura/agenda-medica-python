def test_login_sucesso(client):
    response = client.post("/login", data={
        "email": "admin@timesaver.com.br",
        "password": "senha123"
    }, follow_redirects=False)
    assert response.status_code == 302
    assert "/dashboard" in response.headers["Location"]


def test_login_credenciais_invalidas(client):
    response = client.post("/login", data={
        "email": "admin@timesaver.com.br",
        "password": "senha_errada"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Credenciais invalidas" in response.data


def test_login_usuario_inexistente(client):
    response = client.post("/login", data={
        "email": "naoexiste@test.com",
        "password": "qualquer"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Credenciais invalidas" in response.data


def test_acesso_dashboard_sem_login(client):
    response = client.get("/dashboard", follow_redirects=False)
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


def test_acesso_dashboard_com_login(client):
    client.post("/login", data={
        "email": "admin@timesaver.com.br",
        "password": "senha123"
    })
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert b"Agendamentos" in response.data


def test_logout(client):
    client.post("/login", data={
        "email": "admin@timesaver.com.br",
        "password": "senha123"
    })
    response = client.get("/logout", follow_redirects=False)
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]
