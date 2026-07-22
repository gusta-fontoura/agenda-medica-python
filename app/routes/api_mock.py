import time
from flask import Blueprint, jsonify, request
from app.utils.logger import logger

api_mock_bp = Blueprint("api_mock", __name__)

AGENDAMENTOS_MOCK = [
    {"paciente": "Maria Silva", "cpf": "123.456.789-00", "medico": "Dr. Joao Souza", "especialidade": "Cardiologia", "data": "2026-07-25", "horario": "08:00", "convenio": "Unimed", "status": "Confirmado"},
    {"paciente": "Jose Santos", "cpf": "987.654.321-00", "medico": "Dra. Ana Lima", "especialidade": "Dermatologia", "data": "2026-07-25", "horario": "09:30", "convenio": "Bradesco Saude", "status": "Pendente"},
    {"paciente": "Ana Oliveira", "cpf": "456.789.123-00", "medico": "Dr. Carlos Mendes", "especialidade": "Ortopedia", "data": "2026-07-25", "horario": "10:00", "convenio": "Sulamerica", "status": "Confirmado"},
    {"paciente": "Pedro Ferreira", "cpf": "321.654.987-00", "medico": "Dra. Beatriz Costa", "especialidade": "Pediatria", "data": "2026-07-25", "horario": "11:00", "convenio": "Amil", "status": "Cancelado"},
    {"paciente": "Lucia Martins", "cpf": "789.123.456-00", "medico": "Dr. Joao Souza", "especialidade": "Cardiologia", "data": "2026-07-26", "horario": "08:30", "convenio": "Unimed", "status": "Confirmado"},
    {"paciente": "Roberto Almeida", "cpf": "654.321.987-00", "medico": "Dra. Ana Lima", "especialidade": "Dermatologia", "data": "2026-07-26", "horario": "14:00", "convenio": "Cassi", "status": "Pendente"},
    {"paciente": "Fernanda Rocha", "cpf": "147.258.369-00", "medico": "Dr. Carlos Mendes", "especialidade": "Ortopedia", "data": "2026-07-27", "horario": "09:00", "convenio": "Saude Brasil", "status": "Confirmado"},
    {"paciente": "Marcos Ribeiro", "cpf": "369.258.147-00", "medico": "Dra. Beatriz Costa", "especialidade": "Pediatria", "data": "2026-07-27", "horario": "10:30", "convenio": "Bradesco Saude", "status": "Confirmado"},
    {"paciente": "Claudia Dias", "cpf": "258.369.147-00", "medico": "Dr. Joao Souza", "especialidade": "Cardiologia", "data": "2026-07-28", "horario": "15:00", "convenio": "Sulamerica", "status": "Pendente"},
    {"paciente": "Ricardo Gomes", "cpf": "147.369.258-00", "medico": "Dra. Ana Lima", "especialidade": "Dermatologia", "data": "2026-07-28", "horario": "16:30", "convenio": "Amil", "status": "Confirmado"},
]


@api_mock_bp.route("/api/agendamentos", methods=["GET"])
def get_agendamentos():
    if request.args.get("timeout"):
        logger.info("Simulando timeout na API mock...")
        time.sleep(3)
        return jsonify({"error": "Request timeout"}), 504

    if request.args.get("fail"):
        logger.info("Simulando erro interno na API mock...")
        return jsonify({"error": "Internal server error"}), 500

    if request.args.get("empty"):
        return jsonify([]), 200

    logger.info(f"API mock retornando {len(AGENDAMENTOS_MOCK)} agendamentos.")
    return jsonify(AGENDAMENTOS_MOCK), 200
