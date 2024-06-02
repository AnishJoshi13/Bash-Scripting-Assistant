import streamlit as st
import requests
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from helpers.parsers import extract_code_explanation, extract_code_type1, extract_code_type2
from helpers.inference import run_llama_inference, run_phi_inference_classification, run_phi_inference_explanation

# Set the title of the app
st.title('Bash Scripting Assistant')

# Display a text area for user input
user_input = st.text_area("You:", placeholder="Type your message here...")

# Initialize session state to keep track of the conversation and message count
if "conversation" not in st.session_state:
    st.session_state.conversation = []
    st.session_state.message_count = 0  # Initialize message_count here

# Display previous conversation
for message in st.session_state.conversation:
    st.write(message)

# When the user submits a message
if st.button("Send"):
    if user_input:
        # Add the user's message to the conversation
        st.session_state.conversation.append(f"You: {user_input}")
        st.session_state.message_count += 1

        response = run_llama_inference(user_input)
        try:
            code = extract_code_type1(response)
            if code is None:
                code = response
            code_display = f"""{code}\n\n"""
            #code = "```find . -type f -exec rm {} ;```\n"
            explanation = run_phi_inference_explanation(code)
            explanation = extract_code_explanation(explanation)
            response = code_display + explanation
        except Exception as e:
            print(e, "Running type2")
            response = extract_code_type2(response)


        # Add the response to the conversation
        st.session_state.conversation.append(f"Bot: {response}")
        st.session_state.message_count += 1

        # Clear the conversation history if the message count exceeds the limit
        if st.session_state.message_count > 6:
            st.session_state.conversation = []
            st.session_state.message_count = 0

        # Clear the input text area
        st.experimental_rerun()

    # Display a message when there is no input
    if not user_input:
        st.write("Type your message and press 'Send'.")