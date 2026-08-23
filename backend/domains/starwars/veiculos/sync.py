from backend.database.db import db
from backend.domains.starwars.veiculos.consumer import ConsumerVeiculosApiStarwars
from backend.domains.starwars.veiculos.processor import ProcessorVeiculosApiStarWars
from backend.models.veiculos_api_starwars import VeiculosApiStarWars

class SyncDataBaseVeiculosStarWars:

    def __init__(self):
        self.api_consumer = ConsumerVeiculosApiStarwars()
        self.processor = ProcessorVeiculosApiStarWars()

    def armazenamento_veiculos_starwars_db(self):
        try:
            dados_veiculos = self.api_consumer.get_veiculos()
            veiculos_processados = self.processor.processamento_dados_veiculos(dados_veiculos)

            for veiculo in veiculos_processados:
                if veiculo.external_id is None:
                    continue

                veiculo_existente = db.session.query(VeiculosApiStarWars).filter_by(external_id=veiculo.external_id).first()

                if veiculo_existente is None:
                    db.session.add(veiculo)
                else:
                    veiculo_existente.nome_veiculo = veiculo.nome_veiculo
                    veiculo_existente.modelo = veiculo.modelo
                    veiculo_existente.fabricante = veiculo.fabricante
                    veiculo_existente.custo_creditos = veiculo.custo_creditos
                    veiculo_existente.comprimento = veiculo.comprimento
                    veiculo_existente.velocidade_maxima_atmosfera = veiculo.velocidade_maxima_atmosfera
                    veiculo_existente.tripulacao = veiculo.tripulacao
                    veiculo_existente.passageiros = veiculo.passageiros
                    veiculo_existente.capacidade_carga = veiculo.capacidade_carga
                    veiculo_existente.consumiveis = veiculo.consumiveis
                    veiculo_existente.classe_veiculo = veiculo.classe_veiculo
                    veiculo_existente.data_atualizacao = veiculo.data_atualizacao

            db.session.commit()
            return len(veiculos_processados)

        except Exception as e:
            db.session.rollback()
            raise e
