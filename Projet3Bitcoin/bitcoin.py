import pandas as pd
import pandas_datareader as pdr
import plotly.graph_objects as go

# Récupérer les données du cours BTC-EUR sur les 12 premiers mois
start_date = '2023-01-01'
end_date = '2023-12-31'
btc_eur = pdr.get_data_yahoo("BTC-EUR", start=start_date, end=end_date)

# Créer un graphique de chandelier japonais avec Plotly
fig = go.Figure(data=[go.Candlestick(x=btc_eur.index,
                open=btc_eur['Open'],
                high=btc_eur['High'],
                low=btc_eur['Low'],
                close=btc_eur['Close'])])

# Ajouter un titre au graphique
fig.update_layout(
    title="Graphique de Chandelier Japonais pour BTC-EUR sur les 12 premiers mois",
    xaxis_rangeslider_visible=True  # Ajouter un slider pour l'axe x (date)
)

# Afficher le graphique
fig.show()
