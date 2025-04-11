import streamlit as st

st.set_page_config(page_title="Simple Chatbot", page_icon="🤖")

st.title("Chatbot Web App")

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:", key="input")

def bot_reply(message):
    message = message.lower()
    if "hello" in message:
        return "Hi there! How can I help you?"
    elif "name" in message:
        return "I'm a simple chatbot built with Streamlit!"
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    else:
        return "Sorry, I didn't understand that."

if user_input:
    st.session_state.chat_history.append(("You", user_input))
    reply = bot_reply(user_input)
    st.session_state.chat_history.append(("Bot", reply))

st.markdown("### Conversation")

for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"*{sender}:* {message}")
    else:
        st.markdown(f"{sender}: {message}")
