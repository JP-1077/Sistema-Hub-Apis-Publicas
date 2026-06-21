import requests

class consumer_api_rick_and_morty:
    def __init__(self):
        self.url_api = "https://rickandmortyapi.com/api"


    def get_personagens(self):
        response = requests.get(f"{self.url_api}/character")
        if response.status_code == 200:
            return response.json()
        else:
            return ("Erro na requisição de personagens da API do Rick and Morty")
        

