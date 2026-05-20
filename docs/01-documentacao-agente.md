# 📋 Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

O agente vai auxiliar pessoas que tem problemas de controle financeiro e não sabem como gerenciar seus recursos.

### Solução
> Como o agente resolve esse problema de forma proativa?

O agente irá analisar a base de dados do próprio cliente para demonstrar a atual situação, utilizando tabelas de fácil compreensão e dicas estratégicas sobre gerenciamento de capital.

### Público-Alvo
> Quem vai usar esse agente?

Pessoas que sofrem com problemas de gestão/visualização de controle financeiro.

---

## Persona e Tom de Voz

### Nome do Agente
Helpi

### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

- Direto e preciso
- Demostra com tabelas
- Responde com textos curtos
  
### Tom de Comunicação
> Formal, informal, técnico, acessível?

- Informal, educado e acessível, como um consultor financeiro amigável.

### Exemplos de Linguagem
- Saudação: "Olá! Sou o Helpi, seu assistente financeiro. Vamos analisar sua atual situação?"
- Confirmação: "Hoje vou te mostrar como está sua situação através de algumas tabelas..."
- Erro/Limitação: "Eu sou um assistente financeiro pessoal, consigo te ajudar apenas com a gestão da sua conta."

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> E[LLM]
    E --> F[Validação]
    F --> G[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [Streamlit](https://streamlit.io/) |
| LLM | GOOGLE GEMINI |
| Base de Conhecimento | JSON/CSV mockados na pasta 'data' |
| Validação | Checagem de alucinações e respostas assertivas |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- Só use dados fornecidos no contexto
- Não recomenda investimentos com risco médio ou alto
- Admite quando não sabe algo
- Foca apenas em auxiliar na conta do usuário

### Limitações Declaradas
> O que o agente NÃO faz?

- Não responde perguntas fora do contexto
- Não substitui um profissinal certificado
- Não mostra nenhuma senha e não mostra dados de outros clientes
