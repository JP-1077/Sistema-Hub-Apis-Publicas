import requests

class ConsumerLocalizacaoAPIRickMorty:
    def __init__(self):
        self.url_api = "https://rickandmortyapi.com/api"


    def get_localizacoes(self):
        response = requests.get(f"{self.url_api}/location")
        if response.status_code == 200:
            return response.json()
        else:
            return ("Erro na requisição de localizações da API do Rick and Morty")



        

