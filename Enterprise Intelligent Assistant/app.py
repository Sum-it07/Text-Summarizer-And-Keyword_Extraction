import streamlit as st
from auth import login_flow
# from chatbot import chatbot_ui
from doc_handler import doc_ui

def main():
    st.set_page_config(page_title="Enterprise Intelligent Assistant", layout="wide")

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        # Use login flow from auth.py
        login_flow()
    else:
        st.sidebar.title("Navigation")
        choice = st.sidebar.radio("Go to", ["Document Assistant"])

        # if choice == "Chat":
            # chatbot_ui()
        # elif choice == "Document Assistant":
        doc_ui()

if __name__ == "__main__":
    main()
