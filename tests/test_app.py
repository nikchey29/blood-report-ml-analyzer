import app as app_module


def test_home_page_loads():
    client = app_module.app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_analyze_rejects_missing_fields():
    client = app_module.app.test_client()
    response = client.post("/api/analyze", json={"age": 30})
    assert response.status_code == 400
