from datetime import datetime
from backend.models.veiculos_api_starwars import VeiculosApiStarWars
from backend.domains.starwars.utils import extracao_id_url


class ProcessorVeiculosApiStarWars:

    def processamento_dados_veiculos(self, dados):

        veiculos_processados = []

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

            veiculo = VeiculosApiStarWars(
                external_id = extracao_id_url(item.get("url")),
                nome_veiculo=item.get("name"),
                modelo=item.get("model"),
                fabricante=item.get("manufacturer"),
                custo_creditos=item.get("cost_in_credits"),
                comprimento=item.get("length"),
                velocidade_maxima_atmosfera=item.get("max_atmosphering_speed"),
                tripulacao=item.get("crew"),
                passageiros=item.get("passengers"),
                capacidade_carga=item.get("cargo_capacity"),
                consumiveis=item.get("consumables"),
                classe_veiculo=item.get("vehicle_class"),
                nome_api="StarWars",
                data_criacao=data_criacao,
                data_atualizacao=datetime.utcnow(),
            )

            veiculos_processados.append(veiculo)

        return veiculos_processados
