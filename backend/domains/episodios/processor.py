from backend.models.episodios_rickmorty import Filme
from datetime import datetime

class ProcessamentoDadosEpisodiosAPIRickMorty:
    def procesamento_dados_episodios(self,dados):

        episodios_processados = []

        resultados = dados.get("results", [])

        for item in resultados:
            data_criacao_str = item.get("created")
            data_criacao = datetime.fromisoformat(data_criacao_str.replace("Z", "+00:00")) if data_criacao_str else None

            episodio = Filme(
                external_id = dados.get("id"),
                nome_episodio = dados.get("name"),
                data_lancamento = dados.get("air_date"),
                nomenclatura_episodio = dados.get("episode"),
                personagens = dados.get("characters"),
                url_personagens_episodio = dados.get("url"),
                nome_api = "Rick and Morty",
                data_criacao = data_criacao,
                data_atualizacao = datetime.utcnow() 
            )

            episodios_processados.append(episodio)
            
        return episodios_processados