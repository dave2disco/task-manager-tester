import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, static_folder="../static")

    # Percorso assoluto per il database
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, "..", "instance", "tasks.db")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    from app.routes import tasks_bp
    app.register_blueprint(tasks_bp)

    swagger_bp = get_swaggerui_blueprint(
        "/docs",
        "/static/swagger.json",
        config={"app_name": "Task Manager API"}
    )
    app.register_blueprint(swagger_bp)

    with app.app_context():
        db.create_all()

    return app