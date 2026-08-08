from backend.models.episodios_rickmorty import Filme

class EpisodiosServices:
    def coleta_dados_episodios(self):
        episodios = Filme.query.all()
        resultado_episodios = []

        for episodio in episodios:
            resultado_episodios.append({
                "id": episodio.id,
                "nome_episodio": episodio.nome_episodio,
                "data_lancamento": episodio.data_lancamento,
                "nomenclatura_episodio": episodio.nomenclatura_episodio,
                "url_personagem_episodio": episodio. url_personagens_episodio,
                "api": episodio.nome_api
            })
        return resultado_episodios