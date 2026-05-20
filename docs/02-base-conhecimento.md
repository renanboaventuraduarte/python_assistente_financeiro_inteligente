# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Para que serve o Helpi |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar análises e recomendações baseado nas finanças do cliente |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil, demonstrando de forma didática |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente e demonstrar através de tabelas |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

Os dados foram tratados, adicionado colunas de cálculos e utilizando tabelas para melhor visualização.

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Existem duas possibilidades, injetar os dados diretamente no prompt (Ctrl + C, Ctrl + V) ou carregar os arquivos via código, como no exemplo abaixo:

``` python
import pandas as pd
import json

# CSV
historico = pd.read_csv('data/historico_atendimento.csv')
transacoes = pd.read_csv('data/transacoes.csv')

# JSON
with open("data/perfil_investidor.json','r', econding='utf-8') as f:
	perfil = json.load(f)

with open("data/produto_financeiro.json','r', econding='utf-8') as f:
	produto = json.load(f)
```

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Para simplificar, inserimos os dados em nosso prompt, garantindo que o agente tenha o melhor contexto possível. Em soluções mais robustas, o ideal é que essas informações sejam carregadas dinamicamente de forma automática.

``` text
DADOS E PERFIL DO CLIENTE (data/perfil_investidor.json):

{
  "nome": "João Silva",
  "idade": 32,
  "profissao": "Analista de Sistemas",
  "renda_mensal": 5000.00,
  "perfil_investidor": "moderado",
  "objetivo_principal": "Construir reserva de emergência",
  "patrimonio_total": 15000.00,
  "reserva_emergencia_atual": 10000.00,
  "aceita_risco": false,
  "metas": [
    {
      "meta": "Completar reserva de emergência",
      "valor_necessario": 15000.00,
      "prazo": "2026-06"
    },
    {
      "meta": "Entrada do apartamento",
      "valor_necessario": 50000.00,
      "prazo": "2027-12"
    }
  ]
}

TRANSACOES DO CLIENTE (data/transacoes.csv):

data,descricao,categoria,valor receitas,valor despesas,valor atualizado,tipo
01/10/2025,Salario,receita,R$ 3.000,00,,R$ 3.000,00,ENTRADA
02/10/2025,Aluguel,moradia,,R$ 1.200,00,R$ 1.800,00,SAIDA
03/10/2025,Supermercado,alimentacao,,R$ 450,00,R$ 1.350,00,SAIDA
05/10/2025,Netflix,lazer,,R$ 55,90,R$ 1.294,10,SAIDA
07/10/2025,Farmacia,saude,,R$ 89,00,R$ 1.205,10,SAIDA
10/10/2025,Restaurante,alimentacao,,R$ 120,00,R$ 1.085,10,SAIDA
12/10/2025,Uber,transporte,,R$ 45,00,R$ 1.040,10,SAIDA
15/10/2025,Adiantamento,receita,R$ 2.000,00,,R$ 3.040,10,ENTRADA
15/10/2025,Conta de Luz,moradia,,R$ 180,00,R$ 2.860,10,SAIDA
20/10/2025,Academia,saude,,R$ 99,00,R$ 2.761,10,SAIDA
25/10/2025,Combustivel,transporte,,R$ 250,00,R$ 2.511,10,SAIDA


PRODUTOS DISPONIVEIS (data/produtos_financeiros.json:

[
  {
    "nome": "Tesouro Selic",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "100% da Selic",
    "aporte_minimo": 30.00,
    "indicado_para": "Reserva de emergência e iniciantes"
  },
  {
    "nome": "CDB Liquidez Diária",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "102% do CDI",
    "aporte_minimo": 100.00,
    "indicado_para": "Quem busca segurança com rendimento diário"
  },
  {
    "nome": "LCI/LCA",
    "categoria": "renda_fixa",
    "risco": "baixo",
    "rentabilidade": "95% do CDI",
    "aporte_minimo": 1000.00,
    "indicado_para": "Quem pode esperar 90 dias (isento de IR)"
  },
  {
    "nome": "Fundo Multimercado",
    "categoria": "fundo",
    "risco": "medio",
    "rentabilidade": "CDI + 2%",
    "aporte_minimo": 500.00,
    "indicado_para": "Perfil moderado que busca diversificação"
  },
  {
    "nome": "Fundo de Ações",
    "categoria": "fundo",
    "risco": "alto",
    "rentabilidade": "Variável",
    "aporte_minimo": 100.00,
    "indicado_para": "Perfil arrojado com foco no longo prazo"
  }
]

```
---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

O exemplo de contexto montado abaixo, se baseia nos dados originais da base de conhecimento, sintetizando apenas as informações mais relevantes para otimizar o consumo de tokens. Lembrando que mais importante que economizar tokens é trazer as informações relevantes para o agente.

```
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Saldo disponível: R$ 5.000
- Objetivo: Construir reserva de emergência
- Reserva: R$10.000,00 (meta: R$ 15.000,00)

Resumo de Gastos:
- Moradia: R$ 1.380,00
- Alimentação: R$ 570,00
- Transporte: R$ 295,00
- Saúde: R$ 188,00
- Lazer: R$ 55,90
- Total de Saídas: R$ 2.488,90

Produtos Disponíveis:
- Tesouro Selic (risco baixo)
- CDB Liquidez Diária (risco baixo)
- LCI/LCA (risco baixo)
- Fundo Multimercado (risco médio)
- Fundo de Ações (risco alto)

```
