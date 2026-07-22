# Agenda Medica

Aplicacao web para gestao de agendamentos medicos desenvolvida em Python com Flask.

## Arquitetura

```
Flask App (porta 5000)
├── /login           → Autenticacao via SQLite (werkzeug.security)
├── /dashboard       → Tabela interativa com Tabulator.js
├── /api/agendamentos→ Endpoint mock que retorna JSON simulado
└── Consumo HTTP     → service medical_api.py consome /api/agendamentos via requests
```

### Decisoes Tecnicas

- **Flask + Flask-SQLAlchemy** para backend e ORM
- **SQLite** como banco de dados (leve, sem configuracao externa)
- **Tabulator.js v5** para tabela interativa com busca e formatacao
- **Tailwind CSS** via CDN para estilizacao
- **werkzeug.security** para hash seguro de senhas (pbkdf2)
- **Gunicorn** como WSGI server em producao
- **pytest** para testes automatizados

### Fluxo de Dados

1. Usuario faz login → credenciais validadas contra SQLite
2. Dashboard carrega → frontend requisita dados ao Flask
3. Flask consome internamente `/api/agendamentos` via `requests`
4. Dados retornados ao frontend e renderizados no Tabulator.js
5. Busca instantanea filtra por paciente, CPF ou medico

## Como Rodar

### Com Docker (recomendado)

```bash
docker-compose up --build
```

A aplicacao estara disponivel em: `http://localhost:5000`

### Sem Docker

```bash
pip install -r requirements.txt
python seed.py
python -m flask run
```

## Credenciais de Teste

| Campo | Valor |
|-------|-------|
| E-mail | admin@timesaver.com.br |
| Senha | senha123 |

## Executar Testes

```bash
pytest tests/ -v
```

## Estrutura do Projeto

```
agenda_medica/
├── app/
│   ├── __init__.py          # Factory function create_app()
│   ├── config.py            # Configuracoes via .env
│   ├── models.py            # Modelo User (SQLAlchemy)
│   ├── routes/
│   │   ├── auth.py          # Login/Logout
│   │   ├── main.py          # Dashboard
│   │   └── api_mock.py      # Endpoint mock de agendamentos
│   ├── services/
│   │   └── medical_api.py   # Consumo HTTP da API
│   ├── static/
│   │   ├── js/dashboard.js  # Logica Tabulator.js
│   │   └── css/style.css    # Estilos customizados
│   ├── templates/
│   │   ├── login.html       # Pagina de login
│   │   └── dashboard.html   # Dashboard com tabela
│   └── utils/
│       └── logger.py        # Configuracao de logging
├── tests/
│   ├── conftest.py          # Fixtures pytest
│   ├── test_auth.py         # Testes de autenticacao
│   └── test_api_integration.py # Testes de integracao API
├── seed.py                  # Criacao de tabelas e usuario teste
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .env
```

## Variaveis de Ambiente (.env)

| Variavel | Descricao | Padrao |
|----------|-----------|--------|
| FLASK_SECRET_KEY | Chave secreta da sessao | dev-secret-key-change-in-prod |
| FLASK_PORT | Porta do servidor | 5000 |
| API_MOCK_URL | URL da API mock | http://localhost:5000/api/agendamentos |

## Parametros de Simulacao de Erro

A API mock aceita query params para testes de falha:

- `?fail=true` → Retorna erro 500
- `?timeout=true` → Simula timeout (retorna 504)
- `?empty=true` → Retorna lista vazia
