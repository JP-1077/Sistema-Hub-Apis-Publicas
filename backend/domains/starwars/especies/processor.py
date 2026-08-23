from datetime import datetime
from backend.models.especies_api_starwars import EspeciesApiStarWars
from backend.domains.starwars.utils import extracao_id_url

class ProcessorEspeciesApiStarWars:

    def processamento_dados_especies(self, dados):

        especies_processadas = []

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

            especie = EspeciesApiStarWars(
                id = extracao_id_url(item.get("url")),
                nome=item.get("name"),
                classificacao=item.get("classification"),
                designacao=item.get("designation"),
                altura_media=item.get("average_height"),
                cor_pele=item.get("skin_colors"),
                cor_cabelo=item.get("hair_colors"),
                cor_olhos=item.get("eye_colors"),
                expectativa_vida_media=item.get("average_lifespan"),
                idioma=item.get("language"),
                id_planeta_origem=item.get("homeworld"),
                nome_api="StarWars",
                data_criacao=data_criacao,
                data_atualizacao=datetime.utcnow(),
            )

            especies_processadas.append(especie)

        return especies_processadas
