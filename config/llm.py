"""Configuração do modelo de linguagem."""

from langchain_openai import ChatOpenAI

from config.config import OPENAI_API_KEY


def get_chat_model() -> ChatOpenAI:
    """Cria e retorna instância do modelo de chat.

    Returns:
        ChatOpenAI: Cliente configurado para consultas ao modelo.
    """
    return ChatOpenAI(
        model="gpt-4o-mini",
        api_key=OPENAI_API_KEY,
        temperature=0.2,
    )