import numpy as np
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from autots import AutoTS

data = pd.read_csv("TTM.csv")

#Using Plotly
figure = go.Figure(data=[go.Candlestick(x=data["Date"], open=data["Open"], close=data["Close"], high=data["High"], low=data["Low"])])
figure.update_layout(title = 'Tata Motor Price Analysis', xaxis_rangeslider_visible=True)

model = AutoTS(forecast_length=10, frequency='infer', ensemble='simple')
model = model.fit(data, date_col='Date', value_col='Close', id_col=None)
prediction = model.predict()
forecast = prediction.forecast

print(forecast)
