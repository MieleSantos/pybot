"""Interface web simples do PyBot com Streamlit."""

import sys
from pathlib import Path

import streamlit as st
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from config.errors import handle_openai_error
from config.llm import get_chat_model
from config.logger import logger as _logger
from config.prompts import SYSTEM_PROMPT


def init_state() -> None:
    """Inicializa o estado da conversa no Streamlit.

    Returns:
        None: Popula o session_state com mensagens iniciais.
    """
    if "messages" not in st.session_state:
        st.session_state.messages = [SystemMessage(content=SYSTEM_PROMPT.strip())]


def main() -> None:
    """Executa a interface Streamlit do chatbot.

    Returns:
        None: Renderiza componentes e processa mensagens do usuario.
    """
    st.set_page_config(page_title="PyBot", page_icon="🤖", layout="centered")
    st.title("🤖 PyBot")
    st.caption("Chatbot para tirar duvidas sobre Python.")

    init_state()
    llm = get_chat_model()

    for message in st.session_state.messages:
        if isinstance(message, HumanMessage):
            with st.chat_message("user"):
                st.markdown(message.content)
        elif isinstance(message, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(message.content)

    user_input = st.chat_input("Digite sua duvida de Python...")
    if not user_input:
        return

    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        try:
            response = llm.invoke(st.session_state.messages)
            st.session_state.messages.append(AIMessage(content=response.content))
            st.markdown(response.content)
        except Exception as exc:
            msg = handle_openai_error(exc)
            if msg:
                _logger.error("Erro da OpenAI: {}", exc)
                st.error(msg)
            else:
                _logger.error("Falha inesperada ao consultar o modelo: {}", exc)
                st.error("Erro inesperado ao gerar resposta.")


if __name__ == "__main__":
    main()
