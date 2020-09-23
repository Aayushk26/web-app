
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import numpy as np
import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")


def main():

    st.title('Introduction to Stock Analysis')
    st.subheader('Through this web-app you will learn about some of the widely used indicators')
    st.sidebar.title('Select your technical Indicators')
    st.sidebar.markdown('Here are some Indicators. Any suggestions to improve the web-app are welcomed and appreciated.')

    data = pd.read_csv('^NSEI (1).csv')
    data['Date'] = pd.to_datetime(data['Date'])
    st.markdown('Here is the raw data of the NIFTY 50 Index from NSE. I have chosen this index as it is one of the most volatile indexes in the world.')
    st.markdown('Here is the source of the data : https://in.finance.yahoo.com/quote/%5ENSEI/history?period1=1442966400&period2=1600819200&interval=1d&filter=history&frequency=1d')     
    st.subheader('Created by Aayush D Kandpal')
    st.subheader('⚡ My kaggle profile: https://www.kaggle.com/aayushkandpal')
    st.subheader('👔 Connect with me on LinkedIn : https://www.linkedin.com/in/aayush-kandpal/')

    st.write(data)
    st.subheader('Visualization')
                                
     
    if st.checkbox('Plot the closing prices'):
        st.title('Closing Prices of NIFTY 50 for the last 1 year')
        plt.plot(data['Adj Close'])
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()
    
        
    if st.checkbox('Resources and information about indicators'):
        st.markdown('Hers is an article on Moving Averages https://www.investopedia.com/articles/active-trading/052014/how-use-moving-average-buy-stocks.asp#:~:text=The%20moving%20average%20(MA)%20is,time%20period%20the%20trader%20chooses.')
        st.markdown('Here is an article on Bollinger Bnads https://origin2.cdn.componentsource.com/sites/default/files/resources/dundas/538216/Documentation/Bollinger.html')
        st.markdown('Here is an article on Momentum https://origin2.cdn.componentsource.com/sites/default/files/resources/dundas/538216/Documentation/Bollinger.html')
        st.markdown('Here is an article on different Momentum Indicators https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html')
    if st.sidebar.checkbox('Moving Average 7 Days'):
        data['ma7'] = data['Adj Close'].rolling(window=7).mean()
        plt.plot(data['ma7'],label='MA 7', color='r',linestyle='--')
        plt.plot(data['Adj Close'])
        st.header('Notice the red dotted line, that represents the 7 Day Moving Average for NIFTY 50 for the last year')
        st.pyplot()

    if st.sidebar.checkbox('Moving Average 10 Days'):
        data['ma10'] = data['Adj Close'].rolling(window=10).mean()
        plt.plot(data['ma10'],label='MA 10', color='r',linestyle='--')
        plt.plot(data['Adj Close'])
        st.header('Notice the red dotted line, that represents the 10 Day Moving Average for NIFTY 50 for the last year')
        st.pyplot()

    if st.sidebar.checkbox('Moving Average 20 Days'):
        st.header('Notice the red dotted line, that represents the 20 Day Moving Average for NIFTY 50 for the last year')
        data['ma20'] = data['Adj Close'].rolling(window=20).mean()
        plt.plot(data['ma20'],label='MA 20', color='r',linestyle='--')
        plt.plot(data['Adj Close'])
        st.pyplot()

    if st.sidebar.checkbox('Moving Average 50 Days'):
        st.header('Notice the red dotted line, that represents the 50 Day Moving Average for NIFTY 50 for the last year')
        data['ma50'] = data['Adj Close'].rolling(window=50).mean()
        plt.plot(data['ma50'],label='MA 50', color='r',linestyle='--')
        plt.plot(data['Adj Close'])

        st.pyplot()

    if st.sidebar.checkbox('Moving Average 100 Days'):
        st.header('Notice the red dotted line, that represents the 100 Day Moving Average for NIFTY 50 for the last year')
        st.header('Moving Average 100 days ')
        data['ma100'] = data['Adj Close'].rolling(window=100).mean()
        plt.plot(data['ma100'],label='MA 100', color='r',linestyle='--')
        plt.plot(data['Adj Close'])
        st.pyplot()
        

    if st.sidebar.checkbox('Moving Average Comparison for 7,10,20,50,100 days'):
        st.header('All the moving averages in one view')
        data['ma7'] = data['Adj Close'].rolling(window=7).mean()
        data['ma10'] = data['Adj Close'].rolling(window=10).mean()
        data['ma20'] = data['Adj Close'].rolling(window=20).mean()
        data['ma50'] = data['Adj Close'].rolling(window=50).mean()
        data['ma100'] = data['Adj Close'].rolling(window=100).mean()
        plt.plot(data['ma7'],label='MA 7', color='black',linestyle='--')
        plt.plot(data['ma10'],label='MA 10', color='red',linestyle='--')
        plt.plot(data['ma20'],label='MA 20', color='green',linestyle='-')
        plt.plot(data['ma50'],label='MA 50', color='orange',linestyle='-')
        plt.plot(data['ma100'],label='MA 100', color='blue',linestyle='--')
        plt.plot(data['Adj Close'],label="Closing price")
        plt.legend()
        st.pyplot()

    if st.sidebar.checkbox('Bollinger Bands'):
        st.title('Bollinger Bands')
        data['ma20'] = data['Adj Close'].rolling(window=20).mean()
        data['20sd'] = data['Adj Close'].rolling(window=20).std()
        data['upper_band'] = data['ma20'] + (data['20sd']*2)
        data['lower_band'] = data['ma20'] - (data['20sd']*2)
        plt.plot(data['lower_band'],label='Lower_Band',color='red',linestyle='-')
        plt.plot(data['upper_band'],label='Upper_Band',color='black',linestyle='-')
        plt.plot(data['Adj Close'],label='Closing value',color='green',linestyle='--')
        plt.legend()
        st.set_option('deprecation.showPyplotGlobalUse', False)
        st.pyplot()

if __name__=='__main__':
    main()



    


 



