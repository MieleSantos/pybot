"""Configuracao central de logging com Loguru."""

import sys

from loguru import logger

_configured = False

__all__ = ["logger", "setup_logger"]


def setup_logger() -> None:
    """Configura o logger global da applicacao.

    Executa apenas uma vez. Chamadas subsequentes sao ignoradas.

    Returns:
        None: Aplica configuracao de handlers e formato de logs.
    """
    global _configured
    if _configured:
        return

    logger.remove()
    logger.add(
        sys.stderr,
        level="INFO",
        format=(
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
    )
    _configured = True


setup_logger()
