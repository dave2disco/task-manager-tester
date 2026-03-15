def test_update_task(client):
    """Modifica title e done → 200"""
    client.post("/tasks/", json={"title": "Vecchio titolo"})

    response = client.put("/tasks/1", json={
        "title": "Nuovo titolo",
        "done": True
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["title"] == "Nuovo titolo"
    assert data["done"] == True


def test_update_task_not_found(client):
    """Modifica task inesistente → 404"""
    response = client.put("/tasks/999", json={"title": "X"})
    assert response.status_code == 404