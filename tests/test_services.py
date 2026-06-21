from backend.services.api_consumer_rickmorty import consumer_api_rick_and_morty


def teste_get_personagens():
    api_consumer = consumer_api_rick_and_morty()

    dados = api_consumer.get_personagens()

    print(dados)

teste_get_personagens()


