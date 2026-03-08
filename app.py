import pandas as pd
import streamlit as st
import plotly_express as px

st.header('Vendas de carro')
df_veiculos = pd.read_csv('vehicles.csv')

grafico_hist = st.checkbox("Criar um grafico histograma")
grafico_disper = st.checkbox("Criar gráfico de dispersão")

if grafico_hist:
    st.write(
        'Grágico histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(df_veiculos, x="odometer")
    fig.update_layout(
        xaxis_title="Quilometragem (km)",
        yaxis_title="Quantidade de Carros"
    )
    st.plotly_chart(fig, use_container_width=True)

if grafico_disper:
    st.write(
        'Gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(df_veiculos, x="odometer", y="price",
                     labels={'odometer': 'Quilometragem (km)',
                             'price': 'Preço (R$)'})
    st.plotly_chart(fig, use_container_width=True)
