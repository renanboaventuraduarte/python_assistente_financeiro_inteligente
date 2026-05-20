# 🤖 Helpi — Analista Financeiro Pessoal

Agente de IA para controle e visualização de finanças pessoais. O Helpi analisa os dados do cliente e apresenta sua situação financeira de forma clara, com tabelas e dicas práticas.

---

## 💡 O Problema

Cerca de 80% das famílias brasileiras sofrem com endividamento por não saberem gerenciar seus recursos. O Helpi resolve isso tornando a análise financeira simples e acessível.

---

## 🧠 Como Funciona

```
Cliente → Interface (Streamlit) → LLM (Gemini) → Base de Conhecimento → Resposta
```

O agente carrega os dados do cliente diretamente no contexto do prompt e responde perguntas sobre gastos, metas e produtos financeiros adequados ao perfil.

---

## 📁 Estrutura

```
├── data/
│   ├── perfil_investidor.json       # Perfil e metas do cliente
│   ├── transacoes.csv               # Histórico de transações
│   ├── historico_atendimento.csv    # Atendimentos anteriores
│   └── produtos_financeiros.json   # Produtos disponíveis para sugestão
├── docs/
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
└── src/
    └── app.py                       # Aplicação principal (Streamlit)
```

---

## 🚀 Como Rodar

```bash
# 1. Instalar dependências
pip install streamlit pandas google-genai

# 2. Inserir sua API Key do Gemini em src/app.py
# Localize: client = genai.Client(api_key="SUA_CHAVE_AQUI")

# 3. Rodar a aplicação
streamlit run src/app.py
```

---

## 🛠️ Tecnologias

| Componente | Tecnologia |
|------------|------------|
| Interface  | Streamlit  |
| LLM        | Google Gemini 2.5 Flash |
| Dados      | JSON + CSV (mockados) |

---

## 🔒 Segurança

- Responde **apenas** com dados do cliente fornecidos no contexto
- Não recomenda investimentos de risco alto
- Não exibe dados de outros clientes nem senhas
- Admite quando não tem uma informação

---

## 📊 Exemplos de Uso

| Pergunta | Comportamento esperado |
|----------|----------------------|
| "Como está minha situação hoje?" | Resumo financeiro com tabela |
| "Onde estou gastando mais?" | Gastos por categoria |
| "Qual investimento me recomenda?" | Sugestão compatível com o perfil |
| "Qual a previsão do tempo?" | Redireciona para finanças |

---

## ✅ Resultados

- Assertividade: **5/5** — Respostas corretas baseadas nos dados
- Segurança: **5/5** — Sem alucinações ou informações inventadas
- Coerência: **5/5** — Linguagem clara e acessível

---

> ⚠️ O Helpi não substitui um profissional certificado. Para decisões complexas, consulte um especialista financeiro.
