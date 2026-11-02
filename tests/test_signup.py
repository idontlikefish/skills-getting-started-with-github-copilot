def test_signup_adds_participant(client):
    email = "student@mergington.edu"

    response = client.post(
        "/activities/Soccer Club/signup",
        params={"email": email},
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Signed up student@mergington.edu for Soccer Club"
    }
    assert email in client.get("/activities").json()["Soccer Club"]["participants"]


def test_signup_rejects_duplicate_participant(client):
    email = "student@mergington.edu"
    client.post("/activities/Soccer Club/signup", params={"email": email})

    response = client.post(
        "/activities/Soccer Club/signup",
        params={"email": email},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_rejects_unknown_activity(client):
    response = client.post(
        "/activities/Unknown Club/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_requires_email(client):
    response = client.post("/activities/Soccer Club/signup")

    assert response.status_code == 422
