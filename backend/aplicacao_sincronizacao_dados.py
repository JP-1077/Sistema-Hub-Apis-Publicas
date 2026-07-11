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
from backend.app import create_app
import warnings
import logging
import datetime
from datetime import datetime, timedelta, date

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                                                        # 2. CONFIGURAÇÕES DE LOGS E WARNINGS
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("aplicacao_importacao_quizz_serasa")

warnings.filterwarnings(
    "ignore",
    message="Your application has authenticated using end user credentials",
    category=UserWarning

)

warnings.filterwarnings(
    "ignore",
    message="logger.info area cannot be set to Defined name",
    category=UserWarning
)


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                                                        # 3. SINCRONIZAÇÃO DE DADOS DA API PARA O BANCO DE DADOS
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def sincronizacao_dados_personagens_db():
    app = create_app()
    nome_tabela = "tb_personagem_rick_morty"

    try:
        with app.app_context():
            sync_database_personagem = SyncDatabasePersonagem()
            qtd_personagens_salvos = sync_database_personagem.salvar_personagens_database()
            logger.info(f"A quantidade de personagens salvos na tabela {nome_tabela} foi: {qtd_personagens_salvos}")
    except Exception as e:
        logger.info(f"Erro ao sincronizar os dados da API para a tabela {nome_tabela}: {e}")

def sincronizacao_dados_localizacoes_db():
    app = create_app()
    nome_tabela = "tb_localizacao_rick_morty"

    try:
        with app.app_context():
            sync_database_localizacao = SyncDatabaseLocalizacao()
            qtd_localizacoes_salvos = sync_database_localizacao.salvar_localizacoes_database()
            logger.info(f"A quantidade de localizações salvos na tabela {nome_tabela} foi: {qtd_localizacoes_salvos}")
    except Exception as e:
        logger.info(f"Erro ao sincronizar os dados da API para a tabela {nome_tabela}: {e}")

    
def sincronizacao_dados_episodios_db():
    app = create_app()
    nome_tabela = "tb_episodio_rick_morty"

    try:
        with app.app_context():
            sync_database_episodios = SyncDatabaseEpisodios()
            qtd_episodios_salvos = sync_database_episodios.salvar_episodios_database()
            logger.info(f"A quantidade de episódios salvos na tabela {nome_tabela} foi: {qtd_episodios_salvos}")
    except Exception as e:
        logger.info(f"Erro ao sincronizar os dados da API para a tabela {nome_tabela}: {e}")



#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                                                        # 3. EXECUÇÃO DA APLICAÇÃO
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
def execuca_aplicacao():

    logger.info("========== INÍCIO DO PROCESSO DE SINCRONIZAÇÃO DADOS API PARA DATABASE ==========")
    inicio_execucao = datetime.now()

    try:
        sincronizacao_dados_personagens_db()
        sincronizacao_dados_localizacoes_db()
        sincronizacao_dados_episodios_db()

        logger.info("Processo de sincronização de dados concluído com sucesso.")
    except Exception as e:
        logger.error(f"Ocorreu um erro durante a execução do processo de sincronização de dados: {e}")

    fim_execucao = datetime.now()
    duracao_execucao = fim_execucao - inicio_execucao
    logger.info(f"Duração total da execução: {duracao_execucao}")
    logger.info("========== FIM DO PROCESSO DE SINCRONIZAÇÃO DADOS API PARA DATABASE ==========")


if __name__ == "__main__":
    execuca_aplicacao()
