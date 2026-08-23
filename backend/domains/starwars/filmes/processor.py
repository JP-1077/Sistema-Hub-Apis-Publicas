from backend.models.filmes_api_starwars import Filmesstarwars
from datetime import datetime
from backend.domains.starwars.utils import extracao_id_url
import json


class ProcessorFilmesApiStarWars:

    def processamento_dados_personagem(self,dados):

        filmes_processados = []

        if not dados:
            return []

        if isinstance(dados, dict):
            resultados = dados.get("results", dados.get("data", []))
        else:
            resultados = dados

        for item in resultados:
            data_criacao_str = item.get("created")
            data_criacao = (datetime.fromisoformat(data_criacao_str.replace("Z", "+00:00")) if data_criacao_str else None)

            release_date = item.get("release_date")
            if release_date:
                try:
                    data_lancamento = datetime.strptime(release_date, "%Y-%m-%d").date()
                except ValueError:
                    data_lancamento = None
            else:
                data_lancamento = None

            personagens = item.get("characters") or []
            url_personagens_filme = json.dumps(personagens)

            filmes = Filmesstarwars(
                external_id = extracao_id_url(item.get("url")),
                titulo_filme = item.get("title"),
                episodio = item.get("episode_id"),
                texto_abertura = item.get("opening_crawl"),
                diretor = item.get("director"),
                produtor = item.get("producer"),
                data_lancamento = data_lancamento,
                url_personagens_filme = url_personagens_filme,
                nome_api = "StarWars",
                data_criacao_episodio = data_criacao,
                data_atualizacao = datetime.utcnow()
            )

            filmes_processados.append(filmes)

        return filmes_processados
