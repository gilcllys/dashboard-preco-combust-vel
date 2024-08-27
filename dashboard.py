import math
import streamlit as st
from data import Precos
import matplotlib.pyplot as plt
import seaborn as sns

data = Precos()

st.title('Preços de gasolina em Manaus')
st.write('## Preços por bairro e produto')
opcao_bairro = st.selectbox('Escolha um bairro:', data.get_unique_bairros)
opcao_produto = st.selectbox(
    'Escolha o tipo de produto:', data.get_unique_products)

df_bairro_filtrado = data.get_distrib_preco_by_bairro(
    opcao_bairro, opcao_produto)

# Gráfico de histograma por Bairro de manaus
if df_bairro_filtrado.empty:
    st.write("Sem dados para exibir")
else:
    # Determinando o valor de bins
    n = len(df_bairro_filtrado)
    k = 1 + int(math.log2(n))
    # Crie o gráfico de distribuição
    fig, ax = plt.subplots()
    sns.histplot(df_bairro_filtrado['Valor de Venda'],
                 kde=True, color='blue')

    # Adicione títulos e rótulos
    ax.set_title(
        f'Distribuição dos Preços de {opcao_produto} no Bairro: {opcao_bairro}')
    ax.set_xlabel('Preços')
    ax.set_ylabel('Frequência')

    # Exiba o gráfico no Streamlit
    st.pyplot(fig)
