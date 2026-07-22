import requests as req
from unittest.mock import patch, Mock


def test_api_mock_retorna_agendamentos(client):
    response = client.get("/api/agendamentos")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_api_mock_campos_obrigatorios(client):
    response = client.get("/api/agendamentos")
    data = response.get_json()
    required = ["paciente", "cpf", "medico", "especialidade", "data", "horario", "convenio", "status"]
    for item in data:
        for field in required:
            assert field in item, f"Campo '{field}' ausente no registro"


def test_api_mock_simula_erro(client):
    response = client.get("/api/agendamentos?fail=true")
    assert response.status_code == 500


def test_api_mock_simula_timeout(client):
    response = client.get("/api/agendamentos?timeout=true")
    assert response.status_code == 504


def test_api_mock_lista_vazia(client):
    response = client.get("/api/agendamentos?empty=true")
    data = response.get_json()
    assert data == []


def test_dashboard_carrega_com_dados(client):
    client.post("/login", data={
        "email": "admin@timesaver.com.br",
        "password": "senha123"
    })
    response = client.get("/dashboard")
    assert response.status_code == 200
    assert b"Tabulator" in response.data or b"tabulator" in response.data


def test_consumo_api_falha_retorna_vazio(app, client):
    with patch("app.services.medical_api.requests.get") as mock_get:
        mock_get.side_effect = req.exceptions.ConnectionError("Connection refused")
        with app.app_context():
            from app.services.medical_api import get_agendamentos
            result = get_agendamentos()
            assert result == []


def test_consumo_api_timeout_retorna_vazio(app, client):
    with patch("app.services.medical_api.requests.get") as mock_get:
        mock_get.side_effect = req.exceptions.Timeout("Connection timed out")
        with app.app_context():
            from app.services.medical_api import get_agendamentos
            result = get_agendamentos()
            assert result == []


def test_consumo_api_json_invalido_retorna_vazio(app, client):
    with patch("app.services.medical_api.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.side_effect = ValueError("Invalid JSON")
        mock_get.return_value = mock_response
        with app.app_context():
            from app.services.medical_api import get_agendamentos
            result = get_agendamentos()
            assert result == []


def test_consumo_api_sucesso(app, client):
    mock_data = [
        {"paciente": "Teste", "cpf": "000.000.000-00", "medico": "Dr. Teste",
         "especialidade": "Clinico", "data": "2026-01-01", "horario": "10:00",
         "convenio": "Particular", "status": "Confirmado"}
    ]
    with patch("app.services.medical_api.requests.get") as mock_get:
        mock_response = Mock()
        mock_response.raise_for_status = Mock()
        mock_response.json.return_value = mock_data
        mock_get.return_value = mock_response
        with app.app_context():
            from app.services.medical_api import get_agendamentos
            result = get_agendamentos()
            assert len(result) == 1
            assert result[0]["paciente"] == "Teste"
