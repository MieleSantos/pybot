# PyBot

Chatbot em Python com LangChain + OpenAI, focado em tirar duvidas sobre Python e seguir boas praticas.

## Requisitos

- Python 3.12+
- Poetry instalado

## Configuracao

1. Instale as dependencias:

```bash
poetry install
```

2. Crie/edite o arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_aqui
```

## Executar o projeto

### Opção 1: Interface CLI

```bash
poetry run task run
```

Para encerrar, digite `sair`, `exit` ou `quit`.

### Opção 2: Interface web (Streamlit)

```bash
poetry run task web
```

Depois abra a URL exibida no terminal (geralmente `http://localhost:8501`).

## Comandos de qualidade

- `poetry run task lint` - valida regras do Ruff
- `poetry run task format` - formata codigo com Ruff
- `poetry run task format-check` - valida formatacao sem alterar arquivos
- `poetry run task sort` - organiza imports com isort
- `poetry run task sort-check` - valida imports sem alterar arquivos
- `poetry run task check` - roda lint + format-check + sort-check

## Estrutura do projeto

```text
.
|-- app/
|   |-- chatbot.py     # loop interativo + prompt de sistema
|   |-- main.py        # ponto de entrada da aplicacao CLI
|   `-- streamlit_app.py  # ponto de entrada da aplicacao web
|-- config/
|   |-- config.py     # leitura de variaveis de ambiente
|   |-- errors.py     # tratamento de erros
|   |-- llm.py        # configuracao do LLM
|   |-- logger.py     # configuracao de logs com Loguru
|   `-- prompts.py     # definicao de prompts
|-- pyproject.toml
|-- poetry.lock
|-- README.md
`-- .env
```

## Observacoes

- O bot usa `gpt-4o-mini` por padrao.
- O prompt de sistema foi desenhado para respostas didaticas em portugues.
- Logs da aplicacao sao emitidos com Loguru.
