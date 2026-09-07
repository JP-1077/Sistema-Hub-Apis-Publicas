from backend.models.veiculos_api_starwars import VeiculosApiStarWars


class VeiculosService:

    def coleta_dados_veiculos(self):

        veiculos = VeiculosApiStarWars.query.all()

        resultado_veiculos = []

        for veiculo in veiculos:
            resultado_veiculos.append({
                "id": veiculo.id,
                "Nome Veiculo":veiculo.nome_veiculo,
                "Modelo": veiculo.modelo,
                "Fabricante": veiculo.fabricante,
                "Custo": veiculo.custo_creditos ,
                "Comprimento": veiculo.comprimento,
                "Velocidade Maxima Atmosfera": veiculo.velocidade_maxima_atmosfera,
                "Tripulacao": veiculo.tripulacao,
                "Passageiros": veiculo.passageiros,
                "Capacidade Carga": veiculo.capacidade_carga,
                "Consumiveis": veiculo.consumiveis,
                "Classe Veiculo": veiculo.classe_veiculo,
                "Nome API": veiculo.nome_api,
            })

        return resultado_veiculos