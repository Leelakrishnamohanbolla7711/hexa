import streamlit as st


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Say something:"):
    # Echo user input
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
        # Example response
    response = "Hello! How can I assist you today?"
    with st.chat_message("assistant"):
        st.markdown(response)
