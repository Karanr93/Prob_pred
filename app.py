import streamlit as st
import pandas as pd

# Load the data
data = pd.read_csv('finaloutput.csv', index_col='Customer_ID')

# Title
st.title('Kohler Home Services - Probabilities of Sales Funnel')

# User inputs for Customer ID and Zipcode
customer_id = st.text_input('Enter Customer ID:', '')
zipcode = st.text_input('Enter Zipcode:', '')

# Mapping dictionaries for categorical columns
population_mapping = {1: '<30', 2: '30-40', 3: '40-50',4: '50-60', 5: '60-70', 6: '>70'}
credit_mapping = {1: '<500', 2: '500-550', 3: '550-600',4: '600-650', 5: '650-700', 6: '700-750',7: '750-800', 8: '800-850', 9: '>850'}

call_sentiment = st.text_input('Enter Call Sentiment (1 to 5):', '')
budget = st.text_input('Enter the budget of project:', '')

# Display selected columns
if customer_id and zipcode and call_sentiment and budget :
    try:
        customer_id = int(customer_id)  # Convert input to int
        filtered_data = data[(data.index == customer_id) & (data['zipcode'] == int(zipcode))]
        if not filtered_data.empty:
            filtered_data = filtered_data.replace({'population_agegroup': population_mapping , 'credit_score': credit_mapping})
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
            prob_enq_lead = round(customer_data["probability_enquiry_lead"] *100, 2)
            prob_lead_opp = round(customer_data["probability_lead_opportunity"] *100, 2)
            prob_opp_appoint = round(customer_data["probability_opportunity_appointment"] *100, 2)
            prob_appoint_sale = round(customer_data["probability_appointment_sale"] *100, 2)
            st.write(f'Probability of Enquiry to Lead : {prob_enq_lead}%')
            st.write(f'Probability of Lead to Opportunity : {prob_lead_opp}%')
            st.write(f'Probability of Opportunity to Appointment : {prob_opp_appoint}%')
            st.write(f'Probability of Appointment to Sale : {prob_appoint_sale}%')
        except ValueError:
            st.write('Please enter valid numeric values for Customer ID and Zipcode.')
        except KeyError:
            st.write(f'Customer ID {customer_id} not found in the data.')
    else:
        st.write('Please enter a Customer ID and Zipcode.')

