# -*- coding: utf-8 -*-

import os
import pandas as pd

# **********************************************************
#
# Séries
#
# **********************************************************

idades_dos_alunos = pd.Series([36, 29, 60, 61], index=['Eduardo', 'Heline', 'Cristina', 'Luiz'])

# imprime a média das idades
print("Média:", idades_dos_alunos.mean())

# imprime o desvio padrão das idades
print("Desvio padrão:", idades_dos_alunos.std())

# resume brevemente as estatísticas dos dados
print(idades_dos_alunos.describe())

# eleva ao quadrado com expressão do numpy
print(idades_dos_alunos**2)

# **********************************************************
#
# Data Frame
#
# **********************************************************

# captura o caminho do arquivo de dados
base_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_path, 'data', 'brasil-estados.csv')

# realiza leitura do arquivo CSV
estados = pd.read_csv(file_path, header=0, sep=';')

# imprime a coluna IBGE como Pandas Series
print(estados['IBGE'])

# imprime um DataFrame com as colunas ESTADO e UF
print(estados[['Estado', 'UF']])
