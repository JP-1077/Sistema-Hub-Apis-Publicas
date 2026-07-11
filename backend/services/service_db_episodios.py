from backend.models.episodios_rickmorty import Filme

class EpisodiosServices:


    def coleta_dados_episodios(self):

        episodios = Filme.query.all()
        resultado_episodios = []

        for episodio in episodios:
            resultado_episodios.append({
                "id": episodios.id,
                "nome_episodio": episodios.nome_episodio,
                "data_lancamento": episodios.data_lancamento,
                "nomenclatura_episodio": episodios.nomenclatura_episodio,
                "url_personagem_episodio": episodios. url_personagens_episodio,
                "api": episodios.nome_api
            })
        return resultado_episodios