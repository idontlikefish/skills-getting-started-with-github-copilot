def test_unregister_removes_participant(client):
    email = "michael@mergington.edu"

    response = client.delete(
        "/activities/Chess Club/unregister",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Unregistered michael@mergington.edu from Chess Club"
    }
    assert email not in client.get("/activities").json()["Chess Club"]["participants"]


def test_unregister_rejects_unknown_activity(client):
    response = client.delete(
        "/activities/Unknown Club/unregister",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_rejects_nonparticipant(client):
    response = client.delete(
        "/activities/Soccer Club/unregister",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is not signed up for this activity"
