import pandas as pd
import streamlit as st
import plotly_express as px

st.header('Vendas de carro')
df_veiculos = pd.read_csv('vehicles.csv')
hist_button = st.button('Criar histograma')  # criar um botão

if hist_button:
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(df_veiculos, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

print(df_veiculos)
