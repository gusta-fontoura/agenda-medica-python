from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import User
from app.utils.logger import logger

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if "user_id" in session:
        return redirect(url_for("main.dashboard"))

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if not email or not password:
            flash("Preencha todos os campos.", "error")
            return render_template("login.html")

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session["user_id"] = user.id
            session["user_email"] = user.email
            logger.info(f"Login realizado com sucesso: {user.email}")
            return redirect(url_for("main.dashboard"))

        logger.warning(f"Tentativa de login invalida para: {email}")
        flash("Credenciais invalidas. Verifique seu e-mail e senha.", "error")
        return render_template("login.html")

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():
    user_email = session.get("user_email", "desconhecido")
    session.clear()
    logger.info(f"Logout realizado: {user_email}")
    return redirect(url_for("auth.login"))
