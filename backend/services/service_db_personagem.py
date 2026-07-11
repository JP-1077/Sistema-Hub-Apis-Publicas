from backend.models.personagem_rickmorty import Personagem

class PersonagemService:

    def coleta_dados_personagem(self):
        personagens = Personagem.query.all()

        resultado_personagens = []

        for personagem in personagens:
            resultado_personagens.append({
                "id": personagem.id,
                "name": personagem.nome_personagem,
                "status": personagem.status,
                "especie": personagem.tipo_especie,
                "genero": personagem.genero,
                "imagem": personagem.url_imagem_personagem,
                "api": personagem.nome_api
            })

        return resultado_personagens