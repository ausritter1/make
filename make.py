import streamlit as st
import requests

# Streamlit App
st.title("AI Research Assistant")

# Form for User Input
with st.form(key='input_form'):
    company_name = st.text_input("Company Name:")
    company_website = st.text_input("Company Website:")
    submit_button = st.form_submit_button(label='Run Research Analysis')

# Function to send data to Make webhook
def send_to_make_webhook(company_name, company_website):
    webhook_url = "https://hook.us2.make.com/i4lg6bgna49w8m99ag8e7ezs6vac3csa"  # Replace with your Make webhook URL
    payload = {
        "company_name": company_name,
        "company_website": company_website
    }
    response = requests.post(webhook_url, json=payload)
    return response.json()

# When form is submitted
if submit_button:
    if company_name and company_website:
        st.write("Running analysis for:", company_name)
        response = send_to_make_webhook(company_name, company_website)
        st.write("Analysis results will be displayed below once completed.")

        # Placeholder for result
        result_placeholder = st.empty()

        # Show result based on webhook response
        if response:
            # Update result placeholder
            result_placeholder.write(response)
    else:
        st.warning("Please enter both Company Name and Website.")
