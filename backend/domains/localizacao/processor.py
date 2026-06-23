from backend.models.localizaoes_rickmorty import Planeta
from datetime import datetime

class ProcessamentoDadosLocalizacaoAPIRickMorty:
    def processamento_dados_localizacao(self,dados):

        localizacoes_processadas = []

        resultados = dados.get("results", [])

        for item in resultados:
            data_criacao_str = item.get("created")
            data_criacao = datetime.fromisoformat(data_criacao_str.replace("Z", "+00:00")) if data_criacao_str else None

            localizacao = Planeta(
                external_id = item.get("id"), 
                nome_localizacao = item.get("name"),
                tipo_localizacao = item.get("type"),
                dimensao_localizacao = item.get("dimension"),
                residentes_localizacao = item.get("residents"),
                nome_api = "Rick and Morty",
                data_criacao = data_criacao,
                data_atualizacao = datetime.utcnow() 

            )

            localizacoes_processadas.append(localizacao)

        return localizacoes_processadas

