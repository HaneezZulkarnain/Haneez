import streamlit as st
import pandas as pd

st.title('Rental Real Estate Calculator')

st.sidebar.header('User Input Parameters')

def user_input_features():
    house_price = st.sidebar.slider('House Price', 200000, 2000000, 500000)
    monthly_rent = st.sidebar.slider('Monthly Rent', 1000, 10000, 3000)
    down_payment = st.sidebar.slider('Down Payment', 40000, 400000, 100000)
    longterm_in_years = st.sidebar.slider('Long Term in Years', 1, 30, 30)
    annual_interest = st.sidebar.slider('Annual Interest', 0.00, 10.00, 5.00)
    monthly_taxes = st.sidebar.slider('Monthly Taxes', 0, 1000, 250)

    data = {'house_price'      :  house_price,
            'monthly_rent'     :  monthly_rent,
            'down_payment'     :  down_payment,
            'longterm_in_years':  longterm_in_years,
            'annual_interest'  :  annual_interest,
            'monthly_taxes'    :  monthly_taxes,
    }
    features = pd.DataFrame(data, index=[0])
    return features

# Retrieve user inputs
df = user_input_features()

def calculate_mortgage_payment(annual_interest_rate, years, amount_borrowed):
    
    monthly_interest_rate = annual_interest_rate / 12
    

    monthly_rate_plus_one = 1 + monthly_interest_rate
    
   
    number_of_payments = years * 12
    
   

st.subheader('House Price:')
st.subheader('Down payment (20%):')
st.subheader('Principle:')
st.subheader('Monthly Mortgage:')
st.subheader('Monthly Rent-To-Value:')
st.subheader('Annual Gross Rental:')
st.subheader('Annual Profit:')
