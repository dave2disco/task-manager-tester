def test_create_task_success(client):
    """Crea una task con tutti i campi validi → 201"""
    response = client.post("/tasks/", json={
        "title": "Test task",
        "description": "Descrizione di test"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Test task"
    assert data["done"] == False


def test_create_task_no_title(client):
    """Tenta di creare una task senza title → 400"""
    response = client.post("/tasks/", json={
        "description": "Manca il title"
    })
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_create_task_empty_body(client):
    """Body vuoto → 400"""
    response = client.post("/tasks/", json={})
    assert response.status_code == 400