import yfinance as yf
import streamlit as st
import datetime
st.header("Getting the Stock Name")
stock_name = st.text_input('Input Name of the Stock', 'MSFT')
stock = yf.Ticker(stock_name)

st.header("Stock Prices")
st.write("Currently Analysing ", stock_name, 'stock')

col1, col2 = st.columns(2)
with col1:
    start_date = st.date_input("Enter Start Date", datetime.date(2024, 1, 1))

with col2:
    end_date = st.date_input("Enter end Date", datetime.date(2024, 12, 31))


df = stock.history(start=start_date, end=end_date)
st.write(df)

st.header('Stock Price Trend')
st.line_chart(df['Close'])