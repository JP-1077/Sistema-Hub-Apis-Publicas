import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class ConsumerPersonagensApiDisney:
    def __init__(self):
        self.url_api = "https://api.disneyapi.dev"

        retry = Retry(
            total=4,
            connect=4,
            read=4,
            backoff_factor=2,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET"],
            respect_retry_after_header=True                              ,
        )

        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Sistema-Hub-Apis-Publicas/1.0"})
        self.session.mount("https://", HTTPAdapter(max_retries=retry))

    def get_personagens(self):
        url = f"{self.url_api}/character" 
        parametros = {"page": 1, "pageSize": 50,}
        personagens = []

        while url:
            response = self.session.get(url, params=parametros, timeout=(10, 60),)
            response.raise_for_status()
            dados = response.json()

            if not isinstance(dados, dict):
                raise ValueError("Resposta inesperada da API Disney")

            personagens.extend(dados.get("data", []))

            informacoes = dados.get("info") or {}
            url = informacoes.get("nextPage")
            parametros = None

        return {"data": personagens}


        

