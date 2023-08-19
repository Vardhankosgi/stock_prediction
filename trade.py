from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas_datareader as data
from keras.models import load_model
import streamlit as st
import altair as alt
from altair import Chart
from datetime import datetime
import yfinance as yf


st.title("Stock Price Prediction")
print("please enter the company name for knowing investers data")
user_input = st.text_input('Enter stock Ticker', 'AAPL')
df = yf.download(user_input, start='2021-01-01', end='2022-09-30')

st.subheader('Data from 2021 -2022')
st.write(df.describe())#starting


st.subheader('closing price vs time chart')#ending
plt.xlabel('closing price')
plt.ylabel('time chart')
fig = plt.figure(figsize=(12, 6))
fig = plt.figure(figsize=(13, 8))

plt.plot(df.Close, 'r', label='profit', color="red", linewidth=3)
plt.plot(df.Close, 'b', label='loss', color="blue", linewidth=2)
st.pyplot(fig)
plt.show()

st.subheader('closing P vs time C with 100MA & 200MA(AVERAGE)')
ma100 = df.Close.rolling(30).mean()
ma200 = df.Close.rolling(30).mean()
fig = plt.figure(figsize=(12, 8))

plt.plot(ma100)
plt.plot(ma200)
plt.plot(df.Close)
st.pyplot(fig)
