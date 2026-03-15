# Task Manager Tester

Un progetto portfolio che dimostra competenze di **software testing** su una REST API Python.

## Stack tecnologico
- **Python** + **Flask** — REST API con operazioni CRUD
- **SQLite** + **SQLAlchemy** — Database relazionale
- **pytest** — Suite di test automatici (12 test)
- **Docker** — Containerizzazione dell'applicazione
- **GitHub Actions** — CI pipeline automatica
- **UiPath** — Automazione UI su Swagger

## Come avviare il progetto

### Con Docker
```bash
docker-compose up --build
```

### Senza Docker
```bash
pip install -r requirements.txt
python main.py
```

## Eseguire i test
```bash
pytest tests/ -v
```

## Endpoints API
| Method | URL | Descrizione |
|--------|-----|-------------|
| GET | /tasks/ | Lista tutte le task |
| GET | /tasks/<id> | Recupera una task |
| POST | /tasks/ | Crea una task |
| PUT | /tasks/<id> | Modifica una task |
| DELETE | /tasks/<id> | Elimina una task |

## API pubblica
URL: https://task-manager-tester-mezz.onrender.com
Swagger UI: https://task-manager-tester-mezz.onrender.com/docs