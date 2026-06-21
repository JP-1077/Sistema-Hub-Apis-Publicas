from backend.models.personagem_rickmorty import Personagem
from datetime import datetime


class ProcessamentoDadosAPIRickMorty:
    def processar_dados_personagens(self, dados):
        personagens_processados = []

        resultados = dados.get("results", [])


        for item in resultados:

            data_criacao_str = item.get("created")
            data_criacao = datetime.fromisoformat(data_criacao_str.replace("Z", "+00:00")) if data_criacao_str else None

            personagem  = Personagem(
                external_id = item.get("id"),
                nome_personagem = item.get("name"),
                status = item.get("status"),
                tipo_especie = item.get("species"),
                genero = item.get("gender"),
                url_imagem_personagem = item.get("image"),
                nome_api = "Rick and Morty",
                data_criacao = data_criacao,
                data_atualizacao = datetime.utcnow() 
            )

            personagens_processados.append(personagem)

        return personagens_processados