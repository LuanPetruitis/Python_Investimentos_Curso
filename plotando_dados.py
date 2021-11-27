import matplotlib as mpl
import matplotlib.pyplot as plt
import yfinance as yf
import pandas as pd
import investpy as inv


def grafico(ticker, periodo=None, inicio=None, fim=None, titulo=None, legenda_x=None, legenda_y=None, estilo=None, arquivo=None):
    if periodo is not None:
        dados = yf.Ticker(ticker+'.SA').history(period=periodo)
    elif (inicio is not None) or (fim is not None):
        if (inicio is not None) and (fim is None):
            dados = yf.Ticker(ticker+'.SA').history(start=inicio)
        elif (inicio is None) and (fim is not None):
            dados = yf.Ticker(ticker+'.SA').history(end=fim)
        else:
            dados = yf.Ticker(ticker+'.SA').history(start=inicio, end=fim)
    else:
        dados = yf.Ticker(ticker+'.SA').history(period='6mo')

    x = dados.index
    y = dados['Close']

    mpl.rcParams.update(mpl.rcParamsDefault)

    if estilo is None:
        plt.style.use('tableau-colorblind10')
    else:
        plt.style.use(estilo)

    plt.figure(figsize=(12,5))
    
    plt.plot(x, y)

    estilo_titulo = {
        'family': 'sans-serif',
        'weight':'bold',
        'size':16
    }

    if titulo is None:
        ttl = plt.title('Cotação - ' + ticker, fontdict=estilo_titulo)
    else:
        ttl = plt.title(titulo, fontdict=estilo_titulo)
        
    ttl.set_position([.5, 1.05])

    estilo_legenda = {
        'family': 'sans-serif',
        'weight':'bold',
        'size':12
    }

    if legenda_x is not None:
        plt.xlabel(legenda_x, fontdict=estilo_legenda)
    
    if legenda_y is not None:
        plt.ylabel('Cotação em R$', fontdict=estilo_legenda)
    else:
        plt.ylabel(legenda_y, fontdict=estilo_legenda)

    plt.axis([min(x), max(x), min(y)*0.9, max(y)*1.1])
    
    plt.grid()

    if arquivo is not None:
        plt.savefig(arquivo)
    else:
        plt.show()


# grafico('VALE3')

fundos_investimento = inv.get_funds_list(country="brazil")

# print(fundos_investimento)

resultado_busca = inv.search_funds(by="name", value="Alaska ")
print(resultado_busca['name'][8])

nome_do_fundo = "Alaska Black Institucional Fundo De Investimento De Acoes"
alaska = inv.get_fund_historical_data(nome_do_fundo, country="brazil", from_date='01/01/1500', to_date="15/11/2020")

# print(alaska)

# x = alaska.index
# y = alaska['Close']

# plt.style.use('classic')
# plt.figure(figsize=(12,5))
# plt.plot(x, y)
# plt.title("Cotação do fundo Alaska Black Institucional")
# plt.ylabel("Cotação em reais")
# plt.axis([min(x), max(x), min(y)*0.9, max(y)*1.1])
# plt.grid()
# plt.show()


resultado_busca2 = inv.search_funds(by="name", value="Verde")
print(resultado_busca2['name'][8])

nome_do_fundo2 = "Verde Am V Fundo De Investimento Em Cotas De Fundos De Investimento Multimercado"
verde = inv.get_fund_historical_data(nome_do_fundo2, country="brazil", from_date='01/01/1500', to_date="15/11/2020")

data_inicial = max(min(alaska.index), min(verde.index))

alaska = alaska[alaska.index >= data_inicial]
verde = verde[verde.index >= data_inicial]

alaska['Valorizacao'] = alaska['Close'] / alaska.loc[data_inicial, 'Close']

verde['Valorizacao'] = verde['Close'] / verde.loc[data_inicial, 'Close']

x1 = alaska.index
y1 = alaska['Valorizacao']

x2 = verde.index
y2 = verde['Valorizacao']

plt.style.use('classic')
plt.figure(figsize=(12,5))
plt.plot(x1, y1, label="Alaska Black")
plt.plot(x2, y21, label="Verde")
plt.title("Valorização relativa dos fundos")
plt.grid()
plt.legend(loc="best")
plt.show()