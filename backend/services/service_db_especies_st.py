from backend.models.especies_api_starwars import EspeciesApiStarWars

class EspeciesService:

    def coleta_dados_especies(self):
        especies = EspeciesApiStarWars.query.all()

        resultado_especies = []

        for especie in especies:
            resultado_especies.append({
                "Nome": especie.nome,
                "Classificacao": especie.classificacao,
                "Designacao": especie.designacao,
                "Altura Media": especie.altura_media,
                "Cor da Pele": especie.cor_pele,
                "Cor do Cabelo": especie.cor_cabelo,
                "Cor dos Olhos": especie.cor_olhos,
                "Expectativa de Vida Media": especie.expectativa_vida_media,
                "Idioma": especie.idioma,
                "Id do Planeta de Origem": especie.id_planeta_origem,
                "Nome da API": especie.nome_api,
            })

        return resultado_especies