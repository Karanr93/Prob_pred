import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv('finaloutput.csv', index_col='Customer_ID')

# Title
st.title('Kohler Home Services - Probabilities of Sales Funnel')

# User inputs for Customer ID and Zipcode
customer_id = st.text_input('Enter Customer ID:', '')
zipcode = st.text_input('Enter Zipcode:', '')

# Display selected columns
if customer_id and zipcode:
    try:
        customer_id = int(customer_id)  # Convert input to int
        filtered_data = data[(data.index == customer_id) & (data['zipcode'] == int(zipcode))]
        if not filtered_data.empty:
            st.write(filtered_data[['growthrate_households', 'wealth_index', 'population_agegroup', 'credit_score', 'median_household_income','median_disposable_income','median_net_worth','median_home_value']])
        else:
            st.write('No data found for the given Customer ID and Zipcode.')
    except ValueError:
        st.write('Please enter valid numeric values for Customer ID and Zipcode.')

# Run button
if st.button('Run'):
    if customer_id and zipcode:
        try:
            customer_id = int(customer_id)  # Convert input to int
            customer_data = data.loc[customer_id]
            # Display probabilities
            st.write(f'Probability of Enquiry to Lead : {customer_data["probability_enquiry_lead"]}')
            st.write(f'Probability of Lead to Opportunity : {customer_data["probability_lead_opportunity"]}')
            st.write(f'Probability of Opportunity to Appointment : {customer_data["probability_opportunity_appointment"]}')
            st.write(f'Probability of Appointment to Sale : {customer_data["probability_appointment_sale"]}')
        except ValueError:
            st.write('Please enter valid numeric values for Customer ID and Zipcode.')
        except KeyError:
            st.write(f'Customer ID {customer_id} not found in the data.')
    else:
        st.write('Please enter a Customer ID and Zipcode.')

