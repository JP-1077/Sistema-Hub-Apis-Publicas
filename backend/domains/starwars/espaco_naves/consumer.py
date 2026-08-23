import requests


class ConsumerEspacoNavesApiStarwars:
    def __init__(self):
        self.url_api = "https://swapi.info/api/"

    def get_espaco_naves(self):
        response = requests.get(f"{self.url_api}/starships")

        if response.status_code == 200:
            return response.json()
        else:
            return "Erro na requisição de espaçonaves na API do Star Wars."
