import requests


class ConsumerPersonagensApiStarwars:
    def __init__(self):
        self.url_api = "https://swapi.info/api/"

    def get_personagens(self):
        response = requests.get(f"{self.url_api}/people")

        if response.status_code == 200:
            return response.json()
        else:
            return "Erro na requisição de personagens na API do Star Wars."
