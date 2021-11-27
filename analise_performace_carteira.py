import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd


acoes = ['VALE3.SA', 'GGBR4.SA', 'KLBN4.SA', 'BBAS3.SA', 'USIM5.SA']
pesos = [30, 20, 15, 25, 10]

dados = yf.download(acoes, period='2y')

dados = dados['Adj Close']


# dados['Cota da carteira'] = (
#         dados[acoes[0]]*peso[0] +
#         dados[acoes[1]]*peso[1] +
#         dados[acoes[2]]*peso[2] +
#         dados[acoes[3]]*peso[3] +
#         dados[acoes[4]]*peso[4]
#     ) / 100

dados['Cota da carteira'] = 0 
for acao, peso in zip(acoes, pesos):
    dados['Cota da carteira'] = dados['Cota da carteira'] + (dados[acao]*peso) / 100 

ibov = yf.Ticker('^BVSP').history(period='2y')

comparacao = pd.DataFrame()

comparacao['Valorizacao Ibov'] = ibov['Close'] / ibov.iloc[0]['Close']
comparacao['Valorizacao Carteira'] = dados['Cota da carteira'] / dados.iloc[0]['Cota da carteira']


x1 = comparacao.index
y1 = comparacao['Valorizacao Ibov']

x2 = comparacao.index
y2 = comparacao['Valorizacao Carteira']

plt.style.use('classic')
plt.figure(figsize=(12,5))
plt.plot(x1, y1, label="Ibovespa")
plt.plot(x2, y2, label="Carteira")
plt.title("Comparativo entre a carteira e o Ibovespa")
plt.ylabel("Valorização relativa")
plt.grid()
plt.legend(loc='best')
plt.show()