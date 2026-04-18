"""Ponto de entrada da aplicacao PyBot."""

from app.chatbot import chatbot
from config.logger import logger


def main() -> None:
    """Inicializa e executa o chatbot.

    Returns:
        None: Esta funcao inicia o loop interativo no terminal.
    """
    logger.info("Iniciando aplicacao PyBot.")
    chatbot()


if __name__ == "__main__":
    main()
