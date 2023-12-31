import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('プレ具レスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('右カラム')
expander = st.expander('問い合わせ')
expander.write('問い合わせを書く')

option = st.text_input('あなたの趣味を教えて下さい。')
condition = st.slider('あなたの今の調子は？',0,100,50)
'趣味:', option
'コンディション:', condition