def test_get_activities_returns_activity_details(client):
    response = client.get("/activities")

    assert response.status_code == 200
    activities = response.json()
    assert len(activities) == 9
    assert "Chess Club" in activities

    for activity in activities.values():
        assert set(activity) == {
            "description",
            "schedule",
            "max_participants",
            "participants",
        }
        assert isinstance(activity["participants"], list)
