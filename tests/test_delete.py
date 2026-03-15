def test_delete_task(client):
    """Elimina una task esistente → 200"""
    client.post("/tasks/", json={"title": "Da eliminare"})

    response = client.delete("/tasks/1")
    assert response.status_code == 200
    assert response.get_json()["message"] == "task deleted"


def test_delete_task_not_found(client):
    """Elimina task inesistente → 404"""
    response = client.delete("/tasks/999")
    assert response.status_code == 404


def test_delete_then_get(client):
    """Dopo la cancellazione la task non esiste più → 404"""
    client.post("/tasks/", json={"title": "Da eliminare"})
    client.delete("/tasks/1")

    response = client.get("/tasks/1")
    assert response.status_code == 404