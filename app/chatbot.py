"""Chatbot interativo com LangChain e OpenAI."""

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain.memory import ConversationBufferMemory

from config.errors import handle_openai_error
from config.llm import get_chat_model
from config.logger import logger
from config.prompts import SYSTEM_PROMPT


def create_chat():
    """Cria uma nova conversa com memória de chat."""
    llm = get_chat_model()
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    return ConversationChain(
        llm=llm,
        memory=memory
    )


def chatbot() -> None:
    """Executa o loop interativo do chatbot.

    O bot carrega um prompt de sistema com diretrizes de resposta, recebe
    perguntas do usuario via terminal e envia o historico da conversa para
    o modelo.

    Returns:
        None: Esta funcao apenas executa efeitos colaterais de I/O no terminal.
    """
    llm = get_chat_model()
    messages = [SystemMessage(content=SYSTEM_PROMPT.strip())]

    logger.info("Chatbot inicializado com sucesso.")
    print("PyBot iniciado. Digite 'sair' para encerrar.")

    while True:
        try:
            user_input = input("Voce: ").strip()
        except EOFError:
            logger.warning("Entrada encerrada (EOF). Finalizando chatbot.")
            print("\nBot: Entrada encerrada. Ate mais!")
            break

        if user_input.lower() in {"sair", "exit", "quit"}:
            logger.info("Encerrando chatbot por comando do usuario.")
            print("Ate mais!")
            break
        if not user_input:
            continue

        messages.append(HumanMessage(content=user_input))
        logger.debug("Pergunta recebida do usuario.")
        try:
            response = llm.invoke(messages)
        except Exception as exc:
            msg = handle_openai_error(exc)
            if msg:
                logger.error("Erro da OpenAI: {}", exc)
                print(f"Bot: {msg}\n")
            else:
                logger.error("Falha inesperada ao consultar o modelo: {}", exc)
                print("Bot: Não consegui processar sua pergunta agora. Tente novamente em instantes.\n")
            continue

        messages.append(AIMessage(content=response.content))
        print(f"Bot: {response.content}\n")