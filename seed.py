import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from app import create_app
from app.models import db, User
from app.utils.logger import logger


def seed():
    app = create_app()
    with app.app_context():
        db.create_all()

        existing = User.query.filter_by(email="admin@timesaver.com.br").first()
        if existing:
            logger.info("Usuario de teste ja existe. Seed ignorado.")
            return

        user = User(email="admin@timesaver.com.br")
        user.set_password("senha123")
        db.session.add(user)
        db.session.commit()
        logger.info("Usuario de teste criado: admin@timesaver.com.br / senha123")


if __name__ == "__main__":
    seed()
