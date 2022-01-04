import streamlit as st
import yfinance as yf
import pandas as pd
from PIL import Image

st.write("""
# Simple Stock Price App

***data source:*** Yfinance
""")



st.markdown('<h6 style="float: left;">Shown are the stock closing price and volume of Tesla</h1><img style="float: center;" src="https://www.carlogos.org/car-logos/tesla-logo-2200x2800.png" , width=64 />', unsafe_allow_html=True)


# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0def17e75
#define the ticker symbol

tickerSymbol = 'TSLA'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker

tickerDf = tickerData.history(period= 'id', start='2010-5-31', end='2021-5-31')

#Open High Low Close Volume Dividends Stock Splits


st.write("""
## Closing Price
""")

st.line_chart(tickerDf.Close)

st.write("""
## Volume
""")

st.line_chart(tickerDf.Volume)
