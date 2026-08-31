from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_unregister_participant():
    activity_name = "Chess Club"
    unique_email = "newstudent@mergington.edu"

    response = client.post(f"/activities/{activity_name}/signup?email={unique_email}")
    assert response.status_code == 200

    response = client.delete(f"/activities/{activity_name}/participants/{unique_email}")
    assert response.status_code == 200
    assert unique_email not in client.get("/activities").json()[activity_name]["participants"]


def test_unregister_missing_participant_returns_404():
    response = client.delete("/activities/Chess Club/participants/ghost@mergington.edu")
    assert response.status_code == 404
