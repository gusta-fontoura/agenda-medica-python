import requests
from flask import current_app
from app.utils.logger import logger

REQUIRED_FIELDS = ["paciente", "cpf", "medico", "especialidade", "data", "horario", "convenio", "status"]


class AgendamentoAPIError(Exception):
    def __init__(self, message, status_code=500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


def get_agendamentos():
    url = current_app.config.get("API_MOCK_URL", "http://localhost:5000/api/agendamentos")

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()

        if not isinstance(data, list):
            logger.warning("Resposta da API nao e uma lista.")
            raise AgendamentoAPIError("Formato de resposta inesperado da API.", 502)

        valid_data = []
        for item in data:
            if all(field in item for field in REQUIRED_FIELDS):
                valid_data.append(item)
            else:
                missing = [f for f in REQUIRED_FIELDS if f not in item]
                logger.warning(f"Registro com campos ausentes: {missing}. Registro ignorado.")

        logger.info(f"Consumidos {len(valid_data)} agendamentos validos da API.")
        return valid_data

    except AgendamentoAPIError:
        raise
    except requests.exceptions.Timeout:
        logger.error("Timeout ao conectar com a API de agendamentos.")
        raise AgendamentoAPIError("API de agendamentos indisponivel. Tente novamente mais tarde.", 504)
    except requests.exceptions.ConnectionError:
        logger.error("Erro de conexao com a API de agendamentos.")
        raise AgendamentoAPIError("Nao foi possivel conectar com a API de agendamentos.", 502)
    except requests.exceptions.RequestException as e:
        logger.error(f"Erro na requisicao a API: {e}")
        raise AgendamentoAPIError("Erro ao comunicar com a API de agendamentos.", 502)
    except ValueError:
        logger.error("Resposta da API com JSON invalido.")
        raise AgendamentoAPIError("Resposta invalida da API de agendamentos.", 502)
