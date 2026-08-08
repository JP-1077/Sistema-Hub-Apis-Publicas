import pytest

def test_personagens(client):
    response = client.get("/api/rickmorty/personagem/")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_localizacoes(client):
    response = client.get("/api/rickmorty/localizacao/")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

@pytest.mark.parametrize(
    "url",
    [
        "/api/rickmorty/personagens/",
        "/api/rickmorty/localizacao/",
        "/api/rickmorty/episodios/",
    ],
)

def test_endpoints_rickmort(client, url):
    response = client.get(url)
    assert response.status_code == 200
