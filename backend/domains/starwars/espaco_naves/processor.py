from datetime import datetime
from backend.models.espaco_naves_api_starwars import EspacoNavesApiStarWars
from backend.domains.starwars.utils import extracao_id_url


class ProcessorEspacoNavesApiStarWars:

    def processamento_dados_espaco_naves(self, dados):

        espaco_naves_processadas = []

        if not dados:
            return []

        if isinstance(dados, dict):
            resultados = dados.get("results", dados.get("data", []))
        else:
            resultados = dados

        for item in resultados:
            data_criacao_str = item.get("created")
            data_criacao = (
                datetime.fromisoformat(data_criacao_str.replace("Z", "+00:00"))
                if data_criacao_str
                else None
            )

            espaco_nave = EspacoNavesApiStarWars(
                id = extracao_id_url(item.get("url")), 
                nome=item.get("name"),
                modelo=item.get("model"),
                fabricante=item.get("manufacturer"),
                custo_creditos=item.get("cost_in_credits"),
                comprimento=item.get("length"),
                velocidade_maxima_atmosfera=item.get("max_atmosphering_speed"),
                tripulacao=item.get("crew"),
                passageiros=item.get("passengers"),
                capacidade_carga=item.get("cargo_capacity"),
                consumiveis=item.get("consumables"),
                classificacao_hiperpropulsor=item.get("hyperdrive_rating"),
                mglt=item.get("MGLT"),
                classe_nave=item.get("starship_class"),
                nome_api="StarWars",
                data_criacao=data_criacao,
                data_atualizacao=datetime.utcnow(),
            )

            espaco_naves_processadas.append(espaco_nave)

        return espaco_naves_processadas
