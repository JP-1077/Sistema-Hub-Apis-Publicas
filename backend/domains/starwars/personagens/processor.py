from datetime import datetime
from backend.models.personagens_api_starwars import PersonagemApiStarWars
from backend.domains.starwars.utils import extracao_id_url


class ProcessorPersonagensApiStarWars:

    def processamento_dados_personagens(self, dados):

        personagens_processados = []

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

            personagem = PersonagemApiStarWars(
                external_id = extracao_id_url(item.get("url")),
                nome_personagem=item.get("name"),
                altura=item.get("height"),
                peso=item.get("mass"),
                cor_cabelo=item.get("hair_color"),
                cor_pele=item.get("skin_color"),
                cor_olhos=item.get("eye_color"),
                ano_nascimento=item.get("birth_year"),
                genero=item.get("gender"),
                id_planeta_origem=item.get("homeworld"),
                nome_api="StarWars",
                data_criacao=data_criacao,
                data_atualizacao=datetime.utcnow(),
            )

            personagens_processados.append(personagem)

        return personagens_processados
