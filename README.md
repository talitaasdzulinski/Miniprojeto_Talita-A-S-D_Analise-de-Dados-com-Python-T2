# 📊 Análise Exploratória de Dados — Base Varejo

Projeto do Módulo 1 do curso de Análise de Dados com Python.
A ideia foi aplicar as etapas básicas de uma AED em uma base real de varejo:
identificar problemas nos dados, limpá-los e extrair algumas informações úteis sobre o comportamento de compras.

---

## 📁 Estrutura do Projeto

```
projeto/
├── data/
│   ├── base_varejo.csv           ← base original
│   └── base_varejo_limpa.csv     ← base após limpeza
├── notebooks/
│   └── analise_varejo.ipynb
├── outputs/
│   └── grafico_vendas.png
├── utils/
│   └── funcoes_varejo.py
└── README.md
```

---

## ▶️ Como Executar

1. Clone o repositório:
   ```bash
   git clone (https://github.com/talitaasdzulinski/Miniprojeto_Talita-A-S-D_Analise-de-Dados-com-Python-T2)
   ```
2. Instale as dependências:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
3. Abra e execute o notebook célula por célula:
   ```
   notebooks/analise_varejo.ipynb
   ```

> Também pode ser executado no Google Colab.

---

## 🗃️ Sobre a Base de Dados

- **Fonte:** Kaggle — [Base Varejo](https://www.kaggle.com/datasets/namespaiva/base-varejo/data)
- **Volume:** 830.000 registros originais | 733.447 após limpeza | 14 colunas
- **Período:** Fevereiro de 2019 a Agosto de 2022
- **Colunas principais:** `DATA`, `CO_ID`, `CL_ID`, `CL_GENERO`, `CL_EC`, `CL_FHL`, `CL_SEG`, `PR_ID`, `PR_CAT`, `PR_NOME`

---

## 🔍 Etapas da Análise

1. Carregamento e diagnóstico inicial da base
2. Identificação de problemas: nulos, colunas fantasma e duplicatas
3. Limpeza: remoção de colunas vazias e duplicatas, conversão de datas, tratamento de `#N/D` e padronização de categorias
4. Estatísticas descritivas da coluna `CL_FHL` (número de filhos)
5. Agrupamentos: compras por gênero e itens vendidos por categoria
6. Visualização dos resultados em gráficos

---

## 💡 Insights e Conclusões

1. **Qualidade dos dados**
   A base tinha 4 colunas completamente vazias, 96.553 linhas duplicadas (~11,6% do total)
   e 3.228 registros com `#N/D` nas colunas de categoria e nome do produto.
   Após a limpeza a base ficou com 733.447 registros prontos para análise.

2. **Número de filhos (CL_FHL)**
   A maioria dos clientes não tem filhos — moda e mediana são 0, máximo é 4.
   A média de 1,15 com desvio padrão de 1,42 mostram uma distribuição assimétrica:
   poucos clientes com muitos filhos puxam a média para cima.

3. **Gênero e compras**
   Clientes do gênero feminino compraram um pouco mais: 382.427 itens (52,1%)
   contra 351.020 do masculino (47,9%). A diferença existe mas não é tão grande,
   o que indica boa representatividade dos dois grupos na base.

4. **Categorias mais vendidas**
   Alimentos lidera com 384.197 itens (~52% do total), seguido de Higiene (137.702) e Limpeza (128.632).
   Juntas essas três categorias representam 88,7% das vendas, o que faz sentido para um varejo de consumo básico do dia a dia.

5. **Segmentação de clientes**
   A coluna `CL_SEG` divide os clientes em segmentos A, B e C.
   Cruzar essa informação com volume de compras pode ajudar a identificar
   quais perfis são mais valiosos para estratégias de fidelização.

6. **Problemas remanescentes**
   A base não tem coluna de valor monetário, o que impede calcular receita ou ticket médio.
   O `CO_ID` agrupa vários produtos por compra, mas sem preço unitário não dá pra saber
   o valor de cada transação.

---

## ⚠️ Limitações da Análise

- Sem coluna de preço, não é possível fazer análises financeiras.
- Os critérios de segmentação (A, B, C) não estão documentados na base.
- Os 3.228 registros com `#N/D` foram mantidos como `Sem Categoria` — poderiam ser investigados com mais detalhes.

---

## 👤 Autora

**Talita Aparecida Silva Dzulinski** | Turma 2 | Módulo 1 — Análise de Dados com Python
