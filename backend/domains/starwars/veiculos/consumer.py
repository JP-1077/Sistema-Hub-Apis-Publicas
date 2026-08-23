import requests


class ConsumerVeiculosApiStarwars:
    def __init__(self):
        self.url_api = "https://swapi.info/api/"

    def get_veiculos(self):
        response = requests.get(f"{self.url_api}/vehicles")

        if response.status_code == 200:
            return response.json()
        else:
            return "Erro na requisição de veículos na API do Star Wars."
