"""Configurações de tratamento de erros da API OpenAI."""

from openai import APIConnectionError, AuthenticationError, BadRequestError, RateLimitError


def handle_openai_error(e: Exception) -> str | None:
    """Tratamento centralizado de erros da API OpenAI.

    Args:
        e: Exceção capturada.

    Returns:
        Mensagem de erro amigável ao usuário ou None se erro for desconhecido.
    """
    if isinstance(e, AuthenticationError):
        return "Sua chave OPENAI_API_KEY parece inválida. Revise o .env."
    if isinstance(e, RateLimitError):
        return "Sua conta OpenAI está sem cota ou atingiu limite de uso (erro 429). Verifique billing e limites da API."
    if isinstance(e, APIConnectionError):
        return "Falha de conexão com a OpenAI. Tente novamente."
    if isinstance(e, BadRequestError):
        return "Não foi possível processar esta pergunta (requisição inválida)."
    return None