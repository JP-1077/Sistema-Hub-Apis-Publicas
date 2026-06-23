import requests

class ConsumerEpisodiosAPIRickMorty:
    def __init__(self):
        self.url_api = "https://rickandmortyapi.com/api"


    def get_epsiodios(self):
        response = requests.get(f"{self.url_api}/episode")
        if response.status_code == 200:
            return response.json()
        else:
            return ("Erro na requisição de Episodios da API do Rick and Morty")



        

