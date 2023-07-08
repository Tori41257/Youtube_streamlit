import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title("Streamlit超入門")
st.write('DataFrame')
st.subheader('テスト結果')

df = pd.DataFrame({'Japanese': [55, 96, 76, 82,67],
                   'Mathmatics': [44, 77, 54, 67, 88],
                   'English': [67, 54, 76, 91, 68]})
"""Streamlit_Demo.py

# 章
## 項
### 節
''' python

import streamlit as st
import numpy as np
import pandas as pd

'''
"""
st.write(df)

st.dataframe(df)

st.table(df)

if st.checkbox('Show Image'):
    img = Image.open('google4.png')
    st.image(img, caption = 'Image', use_column_width = True)


option = st.selectbox(
    '数字を選択してください',
    list(range(1,11))
)
'貴方が選んだ数字は',option,'です'

condition = st.sidebar.slider('数字を選択してください',0,100,50) 
'コンディション：',condition

expander = st.expander('お問い合わせ')
expander.write('お問い合わせ内容を書く')