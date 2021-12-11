import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
import mplfinance as mpf


itau = yf.Ticker('ITUB4.SA').history(period='6mo')

# Ajuste do volume para o gráfico
itau2 = itau
itau2['Volume'] = itau2['Volume']/1000000000
# Mostra todos os estilos
# mpf.avaliable_styles()

# Calculando média móvel dos 21 dias
itau2['media21'] = itau2['Close'].rolling(21).mean()


mpf.plot(
    itau2, 
    # Tipo do gráfico
    type='candle', 
    style='yahoo', 
    title='Cotação ITUB4 nos últimos 6 meses', 
    ylabel="Preço em R$", 
    ylabel_lower="Volume \n(em Bilhões de reais)", 
    # Tamanho do gráfico
    figsize=(13,5),
    # Mostrar o volume de negociações  
    volume=True,
    # Mostrar a média 
    mav=(6,9,21),
    # Salva a figura
    savefig='itub.png'
)

# mpf.savefig()