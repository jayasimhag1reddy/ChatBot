import streamlit as st
import requests


API_URL = "http://localhost:8080/chat" # Spring Boot API URL

st.title("Chat with Spring Boot API With DeepSeek-R1 🤖")

user_input = st.text_input("Enter your message:", "") #userinput

if st.button("Send"):
    if user_input.strip():
        try:
            response = requests.get(API_URL, params={"message": user_input})
            if response.status_code == 200:
                st.success("Response: " + response.text)
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")
    else:
        st.warning("Please enter a message.")

