from backend.database.db import db
from backend.domains.starwars.personagens.consumer import ConsumerPersonagensApiStarwars
from backend.domains.starwars.personagens.processor import ProcessorPersonagensApiStarWars
from backend.models.personagens_api_starwars import PersonagemApiStarWars


class SyncDataBasePersonagensStarWars:

    def __init__(self):
        self.api_consumer = ConsumerPersonagensApiStarwars()
        self.processor = ProcessorPersonagensApiStarWars()

    def armazenamento_personagens_starwars_db(self):
        try:
            dados_personagens = self.api_consumer.get_personagens()
            personagens_processados = self.processor.processamento_dados_personagens(dados_personagens)

            for personagem in personagens_processados:
                if personagem.external_id is None:
                    continue

                personagem_existente = db.session.query(PersonagemApiStarWars).filter_by(external_id=personagem.external_id).first()

                if personagem_existente is None:
                    db.session.add(personagem)
                else:
                    personagem_existente.nome_personagem = personagem.nome_personagem
                    personagem_existente.altura = personagem.altura
                    personagem_existente.peso = personagem.peso
                    personagem_existente.cor_cabelo = personagem.cor_cabelo
                    personagem_existente.cor_pele = personagem.cor_pele
                    personagem_existente.nome_personagem = personagem.nome_personagem
                    personagem_existente.cor_olhos = personagem.cor_olhos
                    personagem_existente.ano_nascimento = personagem.ano_nascimento
                    personagem_existente.genero = personagem.genero
                    personagem_existente.id_planeta_origem = personagem.id_planeta_origem
                    personagem_existente.data_atualizacao = personagem.data_atualizacao
                    db.session.add(personagem)

            db.session.commit()
            return len(personagens_processados)

        except Exception as e:
            db.session.rollback()
            raise e
