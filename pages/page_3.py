from matplotlib import pyplot as plt
import pandas as pd
import streamlit as st

#with col2: 予備-ページ分割
    
df=pd.read_csv('./data/data_ex.csv')
st.dataframe(df)
st.table(df)
st.line_chart(df)
st.bar_chart(df)

#matplotlib
fig, ax = plt.subplots()
ax.plot(df.index,df['x'])
st.pyplot(fig)