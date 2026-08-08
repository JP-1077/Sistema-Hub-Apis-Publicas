import requests

class ConsumerPersonagensApiDisney:
    def __init__(self):
        self.url_api = "https://api.disneyapi.dev/"


    def get_personagens(self):
        response = requests.get(f"{self.url_api}/character")
        if response.status_code == 200:
            return response.json()
        else:
            return ("Erro na requisição de personagens da api da Disney.")



        

