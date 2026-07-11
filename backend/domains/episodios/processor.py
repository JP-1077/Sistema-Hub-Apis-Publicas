from backend.models.episodios_rickmorty import Filme
from datetime import datetime

class ProcessamentoDadosEpisodiosAPIRickMorty:
    def processamento_dados_episodios(self, dados):
        episodios_processados = []

        resultados = dados.get("results", [])

        for item in resultados:
            data_criacao_str = item.get("created")
            data_criacao = datetime.fromisoformat(data_criacao_str.replace("Z", "+00:00")) if data_criacao_str else None

            data_lancamento = None
            if item.get("air_date"):
                data_lancamento = datetime.strptime(item.get("air_date"), "%B %d, %Y")

            url_personagens_episodio = ",".join(item.get("characters", [])) if isinstance(item.get("characters"), list) else item.get("characters")

            episodio = Filme(
                external_id=item.get("id"),
                nome_episodio=item.get("name"),
                data_lancamento=data_lancamento,
                nomenclatura_episodio=item.get("episode"),
                url_personagens_episodio=url_personagens_episodio,
                nome_api="Rick and Morty",
                data_criacao_episodio=data_criacao,
                data_atualizacao=datetime.utcnow()
            )

            episodios_processados.append(episodio)

        return episodios_processados