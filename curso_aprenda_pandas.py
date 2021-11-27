import matplotlib.pyplot as plt

import pandas as pd

# dados = pd.read_csv('http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_202011.csv', delimiter=";")

# # Deleta os dados duplicados da coluna indicada
# dados = dados.drop_duplicates('CNPJ_FUNDO')

# # Ordena e pega 5 valores
# top_cotist = dados.sort_values('NR_COTST', ascending=False).head(5)

# dados['Captação líquida'] = dados['CAPTC_DIA'] - dados['RESG_DIA']

# top10_capLiquida = dados.sort_values('Captação líquida', ascending=False).head(10)

# top10_capLiquida.set_index(top10_capLiquida['CNPJ_FUNDO'], inplace=True)

# # print(top_cotist)
# # print(dados)
# # print(top10_capLiquida['Captação líquida'])

# plt.style.use('bmh')

# ax = top10_capLiquida[['CNPJ_FUNDO', 'Captação líquida']].plot(kind='bar', title='Fundos com maiores captações', figsize=(11,5), legend=True, fontsize=12)
# ax.set_xlabel('CNPJ', fontsize=12)
# ax.set_ylabel('Captação Líquida', fontsize=12)

# plt.show()



# DATAFRAME

df1 = pd.DataFrame()

df1['Ação'] = ["VALE3", "BBAS3", "PETR4", "ITSA3", "USIM5", "KLBN4"]
df1['Empresa'] = ["Vale", "Banco do Brasil", "Petrobras", "Itausa", "Usiminas", "Klabin"]
df1['Preço'] = ["60,17", "29,81", "19,79", "10,22", "10,59", "4,89"]
df1['P/L'] = ["49,62", "5,3", "-7,59", "12,28", "-14,61", "-9,68"]
df1['P/VP'] = ["1,7", "0,81", "1,06", "0,98", "9,73", "9,73"]
df1['Div. Yield'] = ["6,4", "5,7", "3,1", "5,4", "0,4", "2"]

print(df1)

df2 = pd.DataFrame({
    'Ação': ["BBAS3", "PETR4", "ITSA3", "USIM5", "KLBN4"],
    'Empresa': ["Banco do Brasil", "Petrobras", "Itausa", "Usiminas", "Klabin"],
    'Preço': ["29,81", "19,79", "10,22", "10,59", "4,89"],
    'P/L': ["5,3", "-7,59", "12,28", "-14,61", "-9,68"],
    'P/VP': ["0,81", "1,06", "0,98", "9,73", "9,73"],
    'Div. Yield': ["5,7", "3,1", "5,4", "0,4", "2"]
})

print(df2)

df3 = pd.read_excel('016 data_frame_acoes.xlsx')

# print(df3)

# Exibindo as primeiras linhas do Data Frame
# print(df3.head())

# Exibindo as últimas linhas do Data Frame
# print(df3.tail())

# Exibindo as informações gerais sobre o Data Frame
# print(df3.shape)
# print(df3.dtypes)
# print(df3.describe())


# # Criar coluna 
# df3['Pontuação'] = df3['Div. Yield'] / (df3['P/L']*df3['P/VP'])

# # print(df3.sort_values(['Pontuação'], ascending=False))
# # print(df3.columns)
# print(df3.loc[range(2, 6)])
# print(df3.loc[df3['Empresa'] == 'Itausa'])

# # Funções para agrupar dados 
# print(df3.groupby('Tipo').sum())
# print(df3.groupby('Tipo').mean())
# print(df3.groupby('Tipo').agg('max'))


# Unindo dataframe

# INNER só mostra os dados que são iguais
print(pd.merge(df1, df2, how='inner'))


# OUTER mostra todos os dados
print(pd.merge(df1, df2, how='outer'))

# LEFT = RIGHT
print(pd.merge(df1, df2, how='left'))

# RIGHT tira as linhas que estão somente na esquerda
print(pd.merge(df1, df2, how='right'))

# concat() só ajunta as tabelas com mesmas colunas
print(pd.concat([df1, df2]).drop_duplicates())
