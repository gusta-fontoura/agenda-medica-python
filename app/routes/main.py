from flask import Blueprint, redirect, url_for, render_template, session

main_bp = Blueprint("main", __name__)


@main_bp.route("/dashboard")
def dashboard():
    if "user_id" not in session:
        return redirect(url_for("auth.login"))
    return render_template("dashboard.html", user_email=session.get("user_email"))
