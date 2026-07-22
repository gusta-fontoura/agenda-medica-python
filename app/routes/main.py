import json
from flask import Blueprint, redirect, url_for, render_template, session
from app.services.medical_api import get_agendamentos, AgendamentoAPIError
from app.utils.logger import logger

main_bp = Blueprint("main", __name__)


@main_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    try:
        agendamentos = get_agendamentos()
    except AgendamentoAPIError as e:
        logger.warning(f"Dashboard: {e.message}")
        return render_template(
            "dashboard.html",
            user_email=session.get("user_email"),
            error_message=e.message,
            agendamentos_json="[]",
        ), e.status_code

    return render_template(
        "dashboard.html",
        user_email=session.get("user_email"),
        agendamentos_json=json.dumps(agendamentos),
    )
