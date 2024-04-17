import streamlit as st
import requests

# Define the base URL of your REST API
BASE_URL = "http://127.0.0.1:5000"

def initialize_chatbot(location):
    url = f"{BASE_URL}/initialize_chatbot"
    data = {"location": location}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return True
    else:
        return False

def execute_result(nl_question):
    url = f"{BASE_URL}/execute_result"
    data = {"nl_question": nl_question}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()["result"]
    else:
        return "Error: Unable to get response from the chatbot."

def main():
    st.title("Theatre Chatbot")

    location = st.text_input("Enter location:")
    if st.button("Initialize Chatbot"):
        if initialize_chatbot(location):
            st.success("Chatbot initialized successfully!")
        else:
            st.error("Failed to initialize chatbot. Please check the location and try again.")

    nl_question = st.text_input("Enter your question:")
    if st.button("Get Answer"):
        result = execute_result(nl_question)
        st.write("Chatbot's Response:")
        st.write(result)

if __name__ == "__main__":
    main()
