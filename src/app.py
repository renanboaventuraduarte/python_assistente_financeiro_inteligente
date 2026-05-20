import json
import os
import pandas as pd
import streamlit as st
from google import genai
from google.genai import types

# ========= CONFIGURAÇÃO DO GEMINI =========
# configuração da API Key do Google Gemini (substitua pela sua chave)
client = genai.Client(api_key="SUA_CHAVE_AQUI")

# Usaremos o modelo recomendado para chat e tarefas gerais de texto
MODELO = "gemini-2.5-flash"

# ========= CARREGAR DADOS =========
perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# ========= MONTAR CONTEXTO =========
contexto = f"""
CLIENTE: {perfil['nome']}, {perfil['idade']} anos, {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMÔNIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# ========= SYSTEM PROMPT =========
SYSTEM_PROMPT = f"""Você é o Helpi, um analista financeiro especializado em controle de gastos.

OBJETIVO:
Seu objetivo é auxiliar o usuário no controle de gastos, demonstrando com tabelas simples a situação atualizada.

REGRAS:
- Sempre baseie suas respostas nos dados fornecidos no CONTEXTO DO CLIENTE.
- Utilize somente os dados do cliente para montar as tabelas.
- Sempre pergunte se o cliente entendeu.
- Nunca invente informações financeiras.
- Jamais responda a perguntas que não estejam relacionadas ao controle de gastos. Quando isso ocorrer, responda lembrando que você é um analista financeiro especializado em controle de gastos e que pode ajudar com isso.
- Utilize linguagem simples, como se explicasse para um amigo.
- Se não souber algo, admita: "Não tenho essa informação, poderia te ajudar de outra forma".

CONTEXTO DO CLIENTE:
{contexto}
"""


# ======== CHAMAR GEMINI =========
def perguntar(msg, historico_chat):
    """Consome a API do Gemini estruturando o histórico de conversa."""
    contents = []

    # Converte o histórico do Streamlit para o Gemini
    for msg_antiga in historico_chat:
        role = "user" if msg_antiga["role"] == "user" else "model"
        contents.append(
            types.Content(
                role=role, parts=[types.Part.from_text(
                    text=msg_antiga["content"])]
            )
        )

    # Adiciona a pergunta atual do usuário
    contents.append(
        types.Content(role="user", parts=[types.Part.from_text(text=msg)])
    )

    try:
        response = client.models.generate_content(
            model=MODELO,
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT,
                temperature=0.3,  # Temperatura baixa para evitar alucinações financeiras
            ),
        )
        return response.text
    except Exception as e:
        return f"Erro ao se comunicar com o Gemini: {e}"


# ========= INTERFACE STREAMLIT =========
st.title("Helpi - Seu Analista Financeiro de Controle de Gastos")

# Inicializa o histórico de chat na sessão do Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibe as mensagens anteriores do histórico
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input do usuário
if pergunta := st.chat_input("Faça uma pergunta sobre seu controle de gastos:"):
    # Mostra a pergunta do usuário
    st.chat_message("user").write(pergunta)

    # Busca e mostra a resposta do assistente (passando o histórico atual)
    with st.spinner("Pensando..."):
        resposta = perguntar(pergunta, st.session_state.messages)
        st.chat_message("assistant").write(resposta)

    # Atualiza o histórico da sessão DEPOIS da resposta para não enviar a pergunta duplicada na mesma iteração
    st.session_state.messages.append({"role": "user", "content": pergunta})
    st.session_state.messages.append(
        {"role": "assistant", "content": resposta})
