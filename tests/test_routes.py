from backend.app import create_app

def test_endpoint_personagem_rickmorty():
    app = create_app()

    client = app.test_client()

    response = client.get(
        "/api/rickmorty/Personagem"
    )

    print(response.get_json())

test_endpoint_personagem_rickmorty()
