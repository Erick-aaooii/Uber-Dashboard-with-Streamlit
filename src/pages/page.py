import streamlit as st
import plotly.express as px
import pandas as pd
from ..utils.kpis import KPIs
from ..utils.charts import ChartsFactory

def show_page():
    
    st.set_page_config(page_title="Dashboard Uber", page_icon="src/assets/uber.png", layout="wide")

    
    df = KPIs.load_data('src/data/ncr_ride_bookings.csv')
    
    total_rides = KPIs.get_total_rides(df)
    completed_rides = KPIs.get_completed_rides(df)
    cancelled_rides = KPIs.get_cancelled_rides(df)
    average_ride_distance = KPIs.get_average_ride_distance(df)
    peak_hours = KPIs.get_peak_hours(df)
    top_pickup_locations = KPIs.get_top_locations(df, 'Pickup Location')
    top_dropoff_locations = KPIs.get_top_locations(df, 'Drop Location')
    payment_method_distribution = KPIs.get_payment_method_distribution(df)
    cancellation_reasons = KPIs.get_cancellation_reasons(df)

    col1, col2, col3, col4 = st.columns(4)

    # Exibindo as métricas nos cartões
    with col1:
        st.metric(label="Total de Corridas", value=total_rides)
    with col2:
        st.metric(label="Corridas Completadas", value=completed_rides)
    with col3:
        st.metric(label="Corridas Canceladas", value=cancelled_rides)
    with col4:
        st.metric(label="Distância Média (km)", value=f"{average_ride_distance:.2f}" if pd.notna(average_ride_distance) else "0")

    st.markdown("## Análises Detalhadas")

    if not peak_hours.empty:
        peak_hours_df = peak_hours.reset_index()
        peak_hours_df.columns = ['Hour', 'Rides']

        peak_hours_fig = ChartsFactory.create_bar_chart(
            data=peak_hours_df,
            x='Hour',
            y='Rides',
            title='Horas de Pico das Corridas',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(peak_hours_fig, use_container_width=True)

    if not top_pickup_locations.empty:
        pickup_df = top_pickup_locations.reset_index()
        pickup_df.columns = ['Pickup Location', 'Count']

        top_pickup_fig = ChartsFactory.create_bar_chart(
            data=pickup_df,
            x='Pickup Location',
            y='Count',
            title='Principais Locais de Pickup',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(top_pickup_fig, use_container_width=True)

    if not top_dropoff_locations.empty:
        dropoff_df = top_dropoff_locations.reset_index()
        dropoff_df.columns = ['Drop Location', 'Count']

        top_dropoff_fig = ChartsFactory.create_bar_chart(
            data=dropoff_df,
            x='Drop Location',
            y='Count',
            title='Principais Locais de Dropoff',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(top_dropoff_fig, use_container_width=True)

    if not payment_method_distribution.empty:
        payment_df = payment_method_distribution.reset_index()
        payment_df.columns = ['Payment Method', 'Count']

        payment_method_fig = ChartsFactory.create_pie_chart(
            data=payment_df,
            values='Count',
            names='Payment Method',
            title='Distribuição dos Métodos de Pagamento',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(payment_method_fig, use_container_width=True)

    if not cancellation_reasons.empty:
        cancel_df = cancellation_reasons.reset_index()
        cancel_df.columns = ['Reason', 'Count']

        cancellation_fig = ChartsFactory.create_bar_chart(
            data=cancel_df,
            x='Reason',
            y='Count',
            title='Razões de Cancelamento',
            color_discrete_sequence=px.colors.qualitative.Pastel
        )
        st.plotly_chart(cancellation_fig, use_container_width=True)
