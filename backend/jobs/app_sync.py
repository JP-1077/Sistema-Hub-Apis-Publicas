#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
                                                            # 1. IMPORTAÇÕES DAS BIBLIOTECAS
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-*/
import sys
from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
from backend.domains.personagem.consumer import consumer_api_rick_and_morty
from backend.domains.localizacao.consumer import ConsumerLocalizacaoAPIRickMorty
from backend.domains.episodios.consumer import ConsumerEpisodiosAPIRickMorty
from backend.domains.personagem.sync import SyncDatabasePersonagem
from backend.domains.localizacao.sync import SyncDatabaseLocalizacao
from backend.domains.episodios.sync import SyncDatabaseEpisodios
from backend.domains.disney.consumer import ConsumerPersonagensApiDisney
from backend.domains.disney.sync import SyncDataBasePersonagensDisney
from backend.domains.starwars.personagens.consumer import ConsumerPersonagensApiStarwars
from backend.domains.starwars.personagens.sync import SyncDataBasePersonagensStarWars
from backend.domains.starwars.planetas.consumer import ConsumerPlanetasApiStarwars
from backend.domains.starwars.planetas.sync import SyncDataBasePlanetasStarWars
from backend.domains.starwars.veiculos.consumer import ConsumerVeiculosApiStarwars
from backend.domains.starwars.veiculos.sync import SyncDataBaseVeiculosStarWars
from backend.domains.starwars.espaco_naves.consumer import ConsumerEspacoNavesApiStarwars
from backend.domains.starwars.espaco_naves.sync import SyncDataBaseEspacoNavesStarWars
from backend.domains.starwars.especies.consumer import ConsumerEspeciesApiStarwars
from backend.domains.starwars.especies.sync import SyncDataBaseEspeciesStarWars
from backend.domains.starwars.filmes.consumer import ConsumerFilmesApiStarwars
from backend.domains.starwars.filmes.sync import SyncDataBaseFilmesStarWars
from backend.app import create_app
import warnings
import logging
import datetime
from datetime import datetime, timedelta, date

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                                                        # 2. CONFIGURAÇÕES DE LOGS E WARNINGS
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("aplicacao_importacao_dados_apis")
warnings.filterwarnings("ignore", message="Your application has authenticated using end user credentials",category=UserWarning)
warnings.filterwarnings("ignore",message="logger.info area cannot be set to Defined name",category=UserWarning)


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                                                        # 3. SINCRONIZAÇÃO DE DADOS DAS APIs
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

def sync_api_disney():
    app = create_app()
    nome_tabela = "tb_personagens_api_disney"

    try:
        with app.app_context():
            sync_api_disney = SyncDataBasePersonagensDisney()
            qtd_personagens_disney_salvo = sync_api_disney.armazenamento_personagens_disney_db()
            logger.info(f"A quantidade de personagens salvos na tabela {nome_tabela} foi: {qtd_personagens_disney_salvo}")
    except Exception as e:
        logger.error(f"Erro ao sincronizar os dados da API Disney para a tabela {nome_tabela}: {e}")


def sync_api_starwars():
    app = create_app()
    tabelas = [
        ("tb_filmes_api_starwars", SyncDataBaseFilmesStarWars(), "armazenamento_filmes_starwars_db"),
        ("tb_personagens_api_starwars", SyncDataBasePersonagensStarWars(), "armazenamento_personagens_starwars_db"),
        ("tb_planetas_api_starwars", SyncDataBasePlanetasStarWars(), "armazenamento_planetas_starwars_db"),
        ("tb_veiculos_api_starwars", SyncDataBaseVeiculosStarWars(), "armazenamento_veiculos_starwars_db"),
        ("tb_espaco_naves_api_starwars", SyncDataBaseEspacoNavesStarWars(), "armazenamento_espaco_naves_starwars_db"),
        ("tb_especies_api_starwars", SyncDataBaseEspeciesStarWars(), "armazenamento_especies_starwars_db"),
    ]

    try:
        with app.app_context():
            for tabela, sincronizador, metodo in tabelas:
                qtd_registros = getattr(sincronizador, metodo)()
                logger.info(f"A quantidade de registros salvos na tabela {tabela} foi: {qtd_registros}")

    except Exception as e:
        logger.error(f"Erro ao sincronizar os dados da API Star Wars: {e}")


def sincronizacao_dados_personagens_db():
    app = create_app()
    nome_tabela = "tb_personagem_rick_morty"

    try:
        with app.app_context():
            sync_database_personagem = SyncDatabasePersonagem()
            qtd_personagens_salvos = sync_database_personagem.salvar_personagens_database()
            logger.info(f"A quantidade de personagens salvos na tabela {nome_tabela} foi: {qtd_personagens_salvos}")
    except Exception as e:
        logger.error(f"Erro ao sincronizar os dados da API para a tabela {nome_tabela}: {e}")

def sincronizacao_dados_localizacoes_db():
    app = create_app()
    nome_tabela = "tb_localizacao_rick_morty"

    try:
        with app.app_context():
            sync_database_localizacao = SyncDatabaseLocalizacao()
            qtd_localizacoes_salvos = sync_database_localizacao.salvar_localizacoes_database()
            logger.info(f"A quantidade de localizações salvos na tabela {nome_tabela} foi: {qtd_localizacoes_salvos}")
    except Exception as e:
        logger.error(f"Erro ao sincronizar os dados da API para a tabela {nome_tabela}: {e}")

    
def sincronizacao_dados_episodios_db():
    app = create_app()
    nome_tabela = "tb_episodio_rick_morty"

    try:
        with app.app_context():
            sync_database_episodios = SyncDatabaseEpisodios()
            qtd_episodios_salvos = sync_database_episodios.salvar_episodios_database()
            logger.info(f"A quantidade de episódios salvos na tabela {nome_tabela} foi: {qtd_episodios_salvos}")
    except Exception as e:
        logger.error(f"Erro ao sincronizar os dados da API para a tabela {nome_tabela}: {e}")



#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                                                        # 3. EXECUÇÃO DA APLICAÇÃO
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def execucao_aplicacao():

    logger.info("========== INÍCIO DO PROCESSO DE SINCRONIZAÇÃO DADOS API PARA DATABASE ==========")
    inicio_execucao = datetime.now()

    try:
        sync_api_disney()
        sync_api_starwars()

        logger.info("Processo de sincronização de dados concluído com sucesso.")
    except Exception as e:
        logger.error(f"Ocorreu um erro durante a execução do processo de sincronização de dados: {e}")

    fim_execucao = datetime.now()
    duracao_execucao = fim_execucao - inicio_execucao
    logger.info(f"Duração total da execução: {duracao_execucao}")
    logger.info("========== FIM DO PROCESSO DE SINCRONIZAÇÃO DADOS API PARA DATABASE ==========")


if __name__ == "__main__":
    execucao_aplicacao()
