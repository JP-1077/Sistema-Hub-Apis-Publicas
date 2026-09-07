from backend.models.filmes_api_starwars import Filmesstarwars


class FilmesService:

    def coleta_dados_filmes(self):

        filmes = Filmesstarwars.query.all()

        resultado_filmes = []

        for filme in filmes:
            resultado_filmes.append({
                "id": filme.id,
                "Titulo": filme.titulo_filme,
                "Episodio": filme.episodio,
                "Texto Abertura": filme.texto_abertura,
                "Diretor": filme.diretor,
                "Produtor": filme.produtor,
                "Data de Lancamento": filme.data_lancamento,
                "Nome API": filme.nome_api,
            })

        return resultado_filmes