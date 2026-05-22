import httpx


def test_get_interactions_returns_200(client: httpx.Client) -> None:
    response = client.get("/interactions/")

    assert response.status_code == 200


def test_get_interactions_response_structure(
    client: httpx.Client,
) -> None:
    response = client.get("/interactions/")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0

    interaction = data[0]

    assert "id" in interaction
    assert "learner_id" in interaction
    assert "item_id" in interaction
    assert "created_at" in interaction
