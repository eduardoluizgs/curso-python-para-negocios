# Básico de Pandas

## O que é o Pandas?

> _[Pandas](https://pandas.pydata.org) é uma biblioteca Python criada para `manipulação` e `análise` em um `conjunto` de dados `estruturados`._

Pandas é uma das portas de entrada para os mundos dos dados devido a sua facilidade de uso e aprendizagem. Pandas é open-source e de uso gratuito, sob uma licença BSD.

Pandas é uma ferramenta de processamento de dados de `alto desempenho`, com recursos flexíveis de `manipulação de planilhas` e de `banco de dados relacionais`.

Pandas pode trabalhar com _"Dados tabulares, como uma planilha Excel ou uma tabela SQL, dados ordenados de modo temporal ou não, matrizes e qualquer outro conjunto de dados, que não necessariamente precisem estar rotulados"._

Pandas é ideal para análises exploratórias de dados, permitindo `leitura`, `manipulação`, `agregação` e `plotagem` dos dados em poucos passos.

Existem dois tipos de estrutura de dados no `pandas`, `séries` e `data frames`, que serão abordados a seguir.

Algumas [vantagens](https://harve.com.br/blog/programacao-python-blog/pandas-python-vantagens-e-como-comecar/) do `Pandas`:

* Suporte para alinhamento automático ou explícito dos dados.
* Tratamento flexível e simplificado de dados ausentes.
* Uso de operações.
* Combinações e operações relacionais.
* Informações estatísticas.
* Séries temporais.
* Visualização de dados.

Caso queria seguir um tutorial passo-a-passo dê uma olhada no site da [W3 Schools](https://www.w3schools.com/python/pandas/default.asp).

Caso queira verificar a documentação da própria biblioteca, execute:

```python
help('pandas')
# Resultado:
# Help on package pandas:

# NAME
#     pandas

# DESCRIPTION
#     pandas - a powerful data analysis and manipulation library for Python
#     =====================================================================

#     **pandas** is a Python package providing fast, flexible, and expressive data
#     ...
```

## Instalação do Pandas

Atualmente `Pandas` possui suporte oficial para Python `3.8`, `3.9` and `3.10`.

Para utilizar o `Pandas` rapidamente basta instalar a biblioteca via `pip`:

```python
pip install pandas
```

Para mais instruções de instalação na [página oficial](https://pandas.pydata.org/docs/getting_started/install.html).

## Instalação do NumPy

> NumPy é uma biblioteca para a linguagem de programação Python, que suporta o processamento de grandes, multi-dimensionais arranjos e matrizes, juntamente com uma grande coleção de funções matemáticas de alto nível para operar sobre estas matrizes. [Wikipedia](https://pt.wikipedia.org/wiki/NumPy)_

NumPy fornece um objeto de `matriz` (array) que é até `50` vezes mais `rápido` que as `listas` tradicionais do Python. Isso é muito importante quando trabalhamos com grandes volumes de dados.

A biblioteca `NumPy` já é instalada com o `Pandas`.

## Series

Um das estruturas de dados do `Pandas` são as `Séries`.

Séries são comparados a `tabelas` simples ou `arrays unidimensionais`, ou ainda uma `lista` simples do Python.

As `séries` podem armazenar dados de qualquer tipo (`inteiro`, `string`, `float`, `objetos python`, etc.).

A estrutura básica de uma `série` pode ser visualizada a abaixo:

```
    | Valor |
| Í |       |
| n |       |
| d |       | Linhas
| i |       |
| c |       |
| e |       |
```

Exemplo:

```
| Índice  | Idade |
| 0       |   36  |
| 1       |   29  |
| 2       |   60  |
| 3       |   61  |
| 4       |   82  |
| 5       |   93  |
```

A seguir temos um exemplo de uma `série` do `Pandas`:

```python
# -*- coding: utf-8 -*-

import pandas as pd

idades_dos_alunos = pd.Series([36, 29, 60, 61])

print(idades_dos_alunos.values)
# Resultado: array([36, 29, 60, 61])

print(idade_dos_alunos)
# Resultado:
# 0 36
# 1 29
# 2 60
# 3 61
# dtype: int64
```

O código acima cria um objeto `Série` do `Pandas`, contendo as idades dos alunos de uma turma.

Como é possível observar ao imprimir todo o objeto no último `print`, o `Pandas` criou um `índice` ou uma `label (rótulo)` específico com inteiros positivos crescentes para nossa `série`, iniciando do número `0` até o número `3`. Isso ocorre por que não informamos `nomes`, `valores` ou `chaves` específicas para nossa série.

```python
idades_dos_alunos = pd.Series([36, 29, 60, 61], index=['Eduardo', 'Heline', 'Cristina', 'Luiz'])

print(idade_dos_alunos)
# Resultado:
# Eduardo   36
# Heline    29
# Cristina  60
# Luiz      61
# dtype: int64
```

O código acima cria uma `série` com índices `nomeados`. Isso facilita o trabalho quando queremos recuperar algum valor da `série`:

```python
# imprime a idade do aluno Eduardo
print(idade_dos_alunos['Eduardo'])
# Resultado: 36
```

Também pode criar uma `série` a partir de um `dicionário` do Python:

```python
idades = {'Eduardo': 36, 'Heline': 29, 'Cristina': 60, 'Luiz': 61}

idades_dos_alunos = pd.Series(idades)

print(idade_dos_alunos)
# Resultado:
# Eduardo   36
# Heline    29
# Cristina  60
# Luiz      61
# dtype: int64
```

Também pode criar uma `série` a partir de um objeto do `NumPy`:

```python
# -*- coding: utf-8 -*-

# cria um numpy.array unidimensional com números pares de 0 a 1000
array_par = np.arange(0, 1001, 2, int)

# crian a serie (serie_par) a partir do array (array_par)
serie_par = pd.Series(array_par)

# imprime as primeiras 5 linhas da série
print(serie_par.head())
# Resultado:
# 0    0
# 1    2
# 2    4
# 3    6
# 4    8
# dtype: int32
```

A partir do objeto `série`, podemos executar algumas operações sobre os dados:

```python
idades_dos_alunos = pd.Series([36, 29, 60, 61], index=['Eduardo', 'Heline', 'Cristina', 'Luiz'])

# imprime a média das idades
print("Média:", idades_dos_alunos.mean())
# Resultado: Média: 46.5

# imprime o desvio padrão das idades
print("Desvio padrão:", idades_dos_alunos.std())
# Resultado: Desvio padrão: 16.421530582338136

# resume brevemente as estatísticas dos dados
print(idades_dos_alunos.describe())
# Resultado:
# count     4.000000
# mean     46.500000
# std      16.421531
# min      29.000000
# 25%      34.250000
# 50%      48.000000
# 75%      60.250000
# max      61.000000
# dtype: float64

# soma mais um ano de vida com expressão do numpy
print(idades_dos_alunos + 1)
# Resultado:
# Eduardo   37
# Heline    30
# Cristina  61
# Luiz      62
# dtype: int64

# eleva ao quadrado com expressão do numpy
print(idades_dos_alunos ** 2)
# Resultado:
# Eduardo     1296
# Heline       841
# Cristina    3600
# Luiz        3721
# dtype: int64
```

## Dataframe

Um `DataFrame (quadro de dados)` é comparado a uma `planilha de excel` ou `tabela do banco de dados`, composto por `colunas`, `linhas` e adicionalmente um `índice`.

Toda `arquivo` lido pelo `Pandas` torna-se um `DataFrame` por padrão.

```
    |            Colunas                 |
    | Coluna A | Coluna B | Coluna N ... |
| Í |          |          |              |
| n |          |          |              |
| d |          |          |              | Linhas
| i |          |          |              |
| c |          |          |              |
| e |          |          |              |
```

## Blibiotecas complementares

A seguir alguns bibliotecas auxiliares que valem a pena dar uma olhada:

* [Seaborn](https://seaborn.pydata.org/): Estatística e visualizações.
* [NumPy](https://numpy.org/): Bibliotecas para funções matemáticas.
* [Matplotlib](https://matplotlib.org/): Visualizações de dados.
* [Scikit-Learn](https://scikit-learn.org/): Classificação, clusterização e regressão.

## Help para os recém chegados

Para você que já programa em `R`, `SQL` e outras liguagens, consulte esse material para veerificar comandos correspondentes no `Pandas`: [Comparison with other tools](https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/index.html).

## Referências

* https://pandas.pydata.org
* https://pt.wikipedia.org/wiki/Pandas_(software)
* http://blog.mds.gov.br/redesuas/lista-de-municipios-brasileiros/
* https://medium.com/data-hackers/uma-introdução-simples-ao-pandas-1e15eea37fa1
* https://www.w3schools.com/python/pandas/default.asp
* https://pt.wikipedia.org/wiki/NumPy
* https://www.codingame.com/playgrounds/52723/programacao-python-parte-3---prof--marco-vaz/pacote-pandas-series
* https://medium.com/tech-grupozap/introdução-a-biblioteca-pandas-89fa8ed4fa38
* https://harve.com.br/blog/programacao-python-blog/pandas-python-vantagens-e-como-comecar/
* 
* 
* 
* 
* 
* 
* 
* 
* 
