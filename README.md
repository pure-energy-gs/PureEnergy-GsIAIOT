# Análise de Consumo de Eletrodomésticos - FIAP 2024

# Integrantes:
- José Ribeiro dos Santos Neto RM 553844
- Keven Ike Pereira da Silva RM 553215
- Vitor Cruz dos Santos RM 553621

## Link do vídeo:
- https://youtu.be/O9v1EJwBFTM

Este projeto tem como objetivo analisar o consumo mensal de energia elétrica de eletrodomésticos, identificar padrões de eficiência e apresentar visualizações interativas para facilitar a tomada de decisões.

---

## Estrutura do Projeto

O projeto é dividido em três partes principais:

1. **Processamento de Dados**
   - Leitura e tratamento de um dataset que contém informações sobre consumo mensal, potência, horas de uso e nome dos eletrodomésticos.
   - Preenchimento de valores ausentes com a mediana do consumo.
   - Categorização dos eletrodomésticos em "Eficiente" e "Ineficiente" com base em um limiar.

2. **Terminal Interativo**
   - Permite ao usuário inserir informações sobre eletrodomésticos e descobrir a categoria de consumo.
   - Possibilita a entrada de múltiplos eletrodomésticos com geração de gráficos comparativos interativos.

3. **Visualizações Interativas**
   - Gráficos interativos criados com Plotly para análise exploratória dos dados do dataset.

---

## Estrutura do Banco de Dados (Dataset)

O dataset utilizado contém as seguintes colunas:

- **CONSUMO_MENSAL_KWH**: Consumo mensal de energia elétrica em kWh.
- **POTENCIA_WATTS**: Potência do eletrodoméstico em watts.
- **HORAS_USO_DIA**: Número de horas de uso diário.
- **NOME_ELETRODOMESTICO**: Nome do eletrodoméstico.
- **CATEGORIA_CONSUMO**: Categoria de eficiência ("Eficiente" ou "Ineficiente").

---

## Funcionalidades

### **Processamento de Dados**
- Preenchimento de valores ausentes no campo `CONSUMO_MENSAL_KWH` com a mediana.
- Categorização dos eletrodomésticos com base em um limiar:
  - **Eficiente**: Consumo abaixo do limiar.
  - **Ineficiente**: Consumo acima do limiar.

### **Terminal Interativo**
- Opção para o usuário inserir dados manuais de eletrodomésticos.
- Comparação de múltiplos eletrodomésticos com gráficos de barras interativos.

### **Visualizações**
1. **Gráfico de Pizza**:
   - Mostra a distribuição entre categorias "Eficiente" e "Ineficiente".
2. **Gráfico de Dispersão**:
   - Relaciona potência e consumo mensal dos eletrodomésticos.
3. **Gráfico de Barras**:
   - Exibe a média de consumo por categoria.

---

## Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Bibliotecas**:
  - `Pandas`: Para manipulação e análise de dados.
  - `Plotly`: Para criação de gráficos interativos.
  - `Colorama`: Para exibição de textos coloridos no terminal.

---

## Exemplos de Gráficos

1. **Gráfico de Pizza**:
   - Distribuição de eletrodomésticos por categoria de consumo.
2. **Gráfico de Barras**:
   - Comparação entre categorias de consumo por potência média.
3. **Gráfico de Dispersão**:
   - Correlação entre consumo mensal e potência dos eletrodomésticos.

---

## Conclusão

Este projeto apresenta uma solução prática e visual para entender o consumo de energia elétrica de eletrodomésticos. Com gráficos interativos e um terminal intuitivo, ele oferece uma experiência completa para análise e categorização de dados, auxiliando na tomada de decisões para economia de energia.

---
