from backend.models.personagens_api_starwars import PersonagemApiStarWars

class PersonagemServiceStarWars:

    def coleta_dados_personagens_st(self):

        personagens_st = PersonagemApiStarWars.query.all()

        resultado_personagens = []

        for personagem in personagens_st:
             resultado_personagens.append({
                "id": personagem.id,
                "Nome do Personagem": personagem.nome_personagem,
                "Altura":personagem.altura,
                "Peso": personagem.peso,
                "Cor do cabelo": personagem.cor_cabelo,
                "Cor da pele": personagem.cor_pele,
                "Cor dos olhos": personagem.cor_olhos,
                "Ano do Nascimento": personagem.ano_nascimento,
                "Gênero": personagem.genero,
                "ID do Planeta de Origem": personagem.id_planeta_origem,
                "Nome da API": personagem.nome_api

             })

        return resultado_personagens
