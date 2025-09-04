import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(page_title="Dashboard Uber", page_icon="./assets/uber.png", layout="wide")

# Carregando os dados
df = pd.read_csv('./data/ncr_ride_bookings.csv')

# Contagem de todos os status de reserva
status_counts = df['Booking Status'].value_counts()

# Criando as colunas
col1, col2, col3 = st.columns(3)

# Exibindo as métricas nos cartões
with col1:
    st.metric(label="Total de Corridas", value=df.shape[0])
with col2:
    st.metric(label="Corridas Completadas", value=status_counts.get('Completed', 0))
with col3:
    st.metric(label="Corridas Canceladas", value=status_counts.get('Incomplete', 0))

#Gráficos
# Criando o gráfico de pizza
fig = px.pie(
    status_counts.reset_index(),
    values='count',
    names='Booking Status',
    title='Proporção dos Status de Corridas'
)

fig2 = px.bar(
    status_counts.reset_index(),
    x='Booking Status',
    y='count',
    title='Contagem por Status de Corridas'
)

fig3 = px.bar(
    df['Driver Cancellation Reason'].dropna().value_counts().reset_index().rename(columns={'index': 'Razão', 'Driver Cancellation Reason': 'Quantidade'}),
    x='Razão',
    y='Quantidade',
    title='Cancelamentos por Cliente'
)

# Gráfico de cancelamentos por motorista
fig4 = px.bar(
    df['Driver Cancellation Reason'].dropna().value_counts().reset_index().rename(columns={'index': 'Razão', 'Driver Cancellation Reason': 'Quantidade'}),
    x='Razão',
    y='Quantidade',
    title='Cancelamentos por Motorista'
)


# Exibindo o gráfico com a largura total do container
with col1:
    st.plotly_chart(fig, use_container_width=True)
with col2:
    st.plotly_chart(fig2, use_container_width=True)
with col3:
    st.plotly_chart(fig3, use_container_width=True)

st.divider()

# Opcional: Mostrar o DataFrame para referência
st.subheader("Visualização dos Dados Brutos")
st.dataframe(df.head())