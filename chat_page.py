import streamlit as st

def main():
    st.title("Chat Page")
    st.write("This is the chat page where users can interact with the chatbot.")

    # Placeholder for chat functionality
    user_input = st.text_input("You:", "")
    if user_input:
        st.write(f"Bot: You said '{user_input}'")

if __name__ == "__main__":
    main()