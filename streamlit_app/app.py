import streamlit as st
import requests

# Base URL of your Flask API
API_URL = "http://127.0.0.1:5000/search"

# Input for search term
search_term = st.text_input("Enter a search term:")

if search_term:
    # Make a request to the Flask API
    response = requests.get(f"{API_URL}/{search_term}")

    # Check if the req
    # uest was successful
    if response.status_code == 200:
        try:
            # Attempt to parse the JSON response
            data = response.json()
            # Process and display the data as needed
            st.write(data)
        except ValueError as e:
            st.error("Error decoding JSON: " + str(e))
            st.write(
                "Response content: " + response.text
            )  # Show raw response content for debugging
    else:
        st.error(f"API request failed with status code {response.status_code}.")
        st.write(
            "Response content: " + response.text
        )  # Show raw response content for debugging
