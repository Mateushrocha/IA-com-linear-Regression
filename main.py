import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

df = pd.read_csv("dados.csv")

modelo = LinearRegression()
x = df[['diametro']]
y = df[['preco']]
modelo.fit(x,y)

st.title("Prevendo o valor de uma Pizza")
st.divider()

diametro = st.number_input("Digite o tamanho do diâmetro da Pizza")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f'Uma pizza com {diametro: }cm vai custar {preco_previsto: 00} ')
