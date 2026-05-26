import plotly.express as px 
import streamlit as st 

def revenue_hbar(data):
    fig = px.bar(
            data,
            x="total_revenue",
            y="product_name",
            orientation="h",          # horizontal bars
            title="Top 10 Products by Revenue",
            height=400,
            text="total_revenue"      # show values on bars
        )
    
    fig.update_layout(
        yaxis=dict(categoryorder="total ascending"),  # sort bars
        xaxis_title="Total Revenue",
        yaxis_title="Product Name",
    )

    st.plotly_chart(fig, use_container_width = True)