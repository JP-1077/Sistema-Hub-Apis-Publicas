import requests


class ConsumerPlanetasApiStarwars:
    def __init__(self):
        self.url_api = "https://swapi.info/api/"

    def get_planetas(self):
        response = requests.get(f"{self.url_api}/planets")

        if response.status_code == 200:
            return response.json()
        else:
            return "Erro na requisição de planetas na API do Star Wars."
