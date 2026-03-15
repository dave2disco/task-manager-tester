import pytest
from app import create_app, db

@pytest.fixture
def app():
    # Crea un'app Flask configurata per il testing
    app = create_app()
    app.config["TESTING"] = True
    # Usa un DB in memoria invece del file tasks.db
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"

    with app.app_context():
        db.create_all()      # Crea le tabelle
        yield app            # Esegui il test
        db.drop_all()        # Pulisci tutto dopo il test

@pytest.fixture
def client(app):
    # Client HTTP per simulare le chiamate all'API
    return app.test_client()