from backend.models.personagens_api_disney import Personagemdisney
from datetime import datetime

class ProcessorPersonagensApiDisney:
    def processamento_dados_personagens(self, dados):

        personagens_processados = []

        if not dados:
            return []

        if isinstance(dados, dict):
            resultados = dados.get("data", dados.get("results", []))
        else:
            resultados = dados

        for item in resultados:
            data_criacao_str = item.get("created")
            data_criacao = datetime.fromisoformat(data_criacao_str.replace("Z", "+00:00")) if data_criacao_str else None

            personagem = Personagemdisney(

                external_id = item.get("_id"),
                filmes = item.get("films"),
                filmes_shorts = item.get("shortFilms"),
                tv_shows = item.get("tvShows"),
                video_games = item.get("videoGames"),
                park_attractions = item.get("parkAttractions"),
                allies = item.get("allies"),
                enemies = item.get("enemies"),
                nome_personagem = item.get("name"),
                url_imagem_personagem = item.get("imageUrl"),
                url_api_personagem = item.get("url"),
                nome_api = "Disney",
                data_criacao_episodio = data_criacao,
                data_atualizacao = datetime.utcnow()
            )

            personagens_processados.append(personagem)

        return personagens_processados
    