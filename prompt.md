# PROMPT PARA DESENVOLVIMENTO DE APLICAÇÃO

**Atue como um Engenheiro de Software Full Stack Sênior especializado em Python (Flask), Arquitetura de Software e DevOps.**

Sua tarefa é gerar a estrutura completa do código e arquivos de configuração para a aplicação **"Agenda Médica"**, atendendo estritamente aos requisitos listados abaixo. O código deve ser limpo, modular, bem documentado e pronto para produção.

---

## 🎯 OBJETIVO DO PROJETO
Desenvolver uma aplicação web de **Agenda Médica** em Python utilizando Flask. A aplicação deve permitir autenticação via banco SQLite, consumir dados de agendamentos via requisições HTTP para uma API simulada, exibir os dados em uma tabela interativa rica em recursos no frontend usando Tabulator, tratar todas as falhas de borda com mensagens amigáveis/logs e ser completamente containerizada via Docker Compose.

---

## 🛠️ TECNOLOGIAS E BIBLIOTECAS OBRIGATÓRIAS
* **Backend:** Python 3.11+, Flask, Flask-SQLAlchemy (ou SQLite nativo/DB API).
* **Banco de Dados:** SQLite (com script de seed para o usuário de teste).
* **Frontend:** HTML5, Tailwind CSS (ou Bootstrap), JS vanilla e a biblioteca **Tabulator.js** para a tabela.
* **Testes:** Pytest (ou unittest).
* **DevOps:** Docker e Docker Compose.

---

## 🏗️ ESTRUTURA DO PROJETO DEVE SEGUIR ESTE PADRÃO:
```text
agenda_medica/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── main.py
│   │   └── api_mock.py      # Servidor mock/endpoint HTTP para agendamentos
│   ├── services/
│   │   └── medical_api.py   # Serviço HTTP que consome a API de agendamentos
│   ├── static/
│   │   ├── js/
│   │   └── css/
│   ├── templates/
│   │   ├── login.html
│   │   └── dashboard.html
│   └── utils/
│       └── logger.py
├── tests/
│   ├── test_auth.py
│   └── test_api_integration.py
├── seed.py                  # Script de criação de tabelas e usuário de teste
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
└── README.md
