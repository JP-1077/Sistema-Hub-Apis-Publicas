from backend.models.localizaoes_rickmorty import Planeta

class LocalizoesServices:

    def coleta_dados_localizoes(self):
        localizacoes = Planeta.query.all()

        resultado_localizacoes = []

        for localizacao in localizacoes:
            resultado_localizacoes.append({
                "id": localizacao.id,
                "nome_localizacao": localizacao.nome_localizacao,
                "tipo_localizacao": localizacao.tipo_localizacao,
                "dimensao": localizacao.dimensao,
                "residentes_localizacao": localizacao.residentes_localizacao,
                "api": localizacao.nome_api
            })

        return resultado_localizacoes


