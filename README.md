# Projeto Car Insurance Claim Prediction

Objetivo: Construir um modelo de classificação para predição dos sinistros.

O conjunto de dados contém várias informações sobre segurados e a variável target (outcome) indica se o segurado terá um sinistro (ou não) nos próximos 6 meses. Há um script Python intitulado Claims.ipynb para ajudá-los a fazer a leitura do arquivo csv.

### Dados de treinamento e test dos modelos de ML:
* Divida os dados em 80% para treinamento e 20% para teste.

## Tarefas a serem feitas
1. Aplicar lowercase em todas as colunas;
2. Excluir caracteres especiais dos nomes das colunas;
3. Tratamento dos outliers;
4. Tratamento dos missing values;
5. Lidar com dados categóricos;
6. Fazer EDA (Análise Expploratória de Dados);
7. Seleção de features;
8. Definir as amostras de treinamento e validação;
9. Escolher o algoritmo a ser aplicado;
10. Métricas de performance dos algoritmos;
11. Selecionar o melhor modelo preditivo;

## Como Executar o Projeto
1. Clone o repositório:
```
git clone [<url-do-repositorio>](https://github.com/alexmsza/prevsinsegauto)
```
2. Crie e ative um ambiente virtual:
```
python -m venv .venv
source .venv/Scripts/activate
```
3. Instale as dependências:
```
pip install -r requirements.txt
```
4. Execute o notebook Jupyter:
```
papermill PrevSinSegAuto.ipynb PrevSinSegAuto_output.ipynb
```
5. Abra o arquivo `index.html` para ver os resultados:
```
start index.html
```