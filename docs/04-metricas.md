# Métricas e Resultados

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [x] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto BBDC3 na Bovespa?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [x] Correto  [ ] Incorreto

---

## Formulário de Feedback

| Métrica | Pergunta | Nota (1-5) |
|---------|----------|------------|
| Assertividade | "O retorno respondeu sua pergunta?" | 5 |
| Segurança | "As informações pareceram confiáveis?" | 5 |
| Coerência | "A linguagem foi clara e fácil de entender?" | 5 |

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- Funcionou, trazendo as informações corretas e de forma simples.
- Mostrou de forma analítica sugestões precisas de como gerenciar meu dinheiro.

**O que pode melhorar:**
- Poderia criar dashboards para facilitar visualização da situação atual da conta.

---
