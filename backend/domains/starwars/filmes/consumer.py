import requests

class ConsumerFilmesApiStarwars:
    def __init__(self):
        self.url_api = "https://swapi.info/api/"

    def get_filmes(self):
        response = requests.get(f"{self.url_api}/films")

        if response.status_code == 200:
            return response.json()
        else:
            return ("Erro na requisição de filmes na API do Star Wars.")