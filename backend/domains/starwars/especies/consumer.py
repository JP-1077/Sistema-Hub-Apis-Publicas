import requests


class ConsumerEspeciesApiStarwars:
    def __init__(self):
        self.url_api = "https://swapi.info/api/"

    def get_especies(self):
        response = requests.get(f"{self.url_api}/species")

        if response.status_code == 200:
            return response.json()
        else:
            return "Erro na requisição de espécies na API do Star Wars."
