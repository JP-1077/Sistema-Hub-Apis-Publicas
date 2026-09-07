from backend.models.espaco_naves_api_starwars import EspacoNavesApiStarWars

class EspacoNavesService:

    def coleta_dados_naves(self):
        naves = EspacoNavesApiStarWars.query.all()

        resultado_naves = []

        for nave in naves:
            resultado_naves.append({
                "Nome": nave.nome,
                "Modelo": nave.modelo,
                "Fabricante": nave.fabricante,
                "Custo em Créditos": nave.custo_creditos,
                "Comprimento": nave.comprimento,
                "Velocidade Maxima na Atmosfera": nave.velocidade_maxima_atmosfera,
                "Tripulação": nave.tripulacao,
                "Passageiros": nave.passageiros,
                "Capacidade de Carga": nave.capacidade_carga,
                "Consumiveis": nave.consumiveis,
                "Classificacao Hiperpropulsor": nave.classificacao_hiperpropulsor,
                "Mglt": nave.mglt,
                "Classe": nave.classe_nave,
                "Nome da API": nave.nome_api,
            })

        return resultado_naves