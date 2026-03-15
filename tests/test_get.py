def test_get_all_tasks_empty(client):
    """Lista vuota quando non ci sono task → 200"""
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert response.get_json() == []


def test_get_all_tasks(client):
    """Crea 2 task e verifica che vengano restituite → 200"""
    client.post("/tasks/", json={"title": "Task 1"})
    client.post("/tasks/", json={"title": "Task 2"})

    response = client.get("/tasks/")
    assert response.status_code == 200
    assert len(response.get_json()) == 2


def test_get_single_task(client):
    """Recupera una task per ID → 200"""
    client.post("/tasks/", json={"title": "Task singola"})

    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.get_json()["title"] == "Task singola"


def test_get_task_not_found(client):
    """ID inesistente → 404"""
    response = client.get("/tasks/999")
    assert response.status_code == 404