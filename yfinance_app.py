import streamlit as st
import pandas as pd
import yfinance as yf
import altair as alt

st.title("組長マネジメントボード用技術開発デモ")

st.sidebar.write(
    """
    # 米国株価(GAFA)可視化アプリ
    """
)

st.sidebar.write(
    """
    ## 表示日数選択
    """
)

days = st.sidebar.slider('日数',1,50,20) 

st.write(
    f"""
    ## 過去{days}日間のGAFAの株価
    """
)

@st.cache_resource
def get_data(days,tickers):
    df = pd.DataFrame()
    for company in tickers.keys():
        #print(company)
        tkr = yf.Ticker(tickers[company])
        hist = tkr.history(period=f'{days}d')
        hist.index = hist.index.strftime('%d %B %Y')
        hist = hist[['Close']]
        hist.columns = [company]
        hist = hist.T
        hist.index.name = 'Name'
        df = pd.concat([df,hist])
    return df
try: 
    st.write(
        """
        ## 株価の範囲指定
        """
    )

    ymin,ymax = st.sidebar.slider('範囲を指定してください',0.0,3500.0,(0.0,3500.0))

    tickers = {
        'apple':'AAPL',
        'Microsoft':'MSFT',
        'google':'GOOGL',
        'Amazon':'AMZN'
    }

    df = get_data(days,tickers)

    companies = st.multiselect(
        '会社名を選択してください',
        list(df.index),
        ['google','apple','Microsoft','Amazon']
    )

    if not companies:
        st.error('少なくとも1社は選んでください')

    else:
        data = df.loc[companies]
        st.write('### 株価(USD)',data.sort_index())
        data = data.T.reset_index()
        data = pd.melt(data, id_vars=['Date']).rename(
            columns = {'value':'Stock Prices(USD)'}
        )

        chart = (
            alt.Chart(data)
            .mark_line(opacity = 0.8,clip=True)
            .encode(
                x="Date:T",
                y=alt.Y("Stock Prices(USD):Q",stack = None, scale = alt.Scale(domain=[ymin,ymax])),
                color = 'Name:N'
            )
        )
        st.altair_chart(chart, use_container_width=True)

except:
    st.error(
        "おっと！なにかエラーが起きているようです。"
    )