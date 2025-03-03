import streamlit as st
import hashlib
from utils.database import create_user, get_user

def main():
    st.title("Sign Up for the RAG Chatbot")

    # If already logged in, show a warning and allow logout
    if "username" in st.session_state:
        st.warning("You are already logged in. Log out first if you want to create a new account.")
        if st.button("Log out"):
            del st.session_state["username"]
            del st.session_state["role"]
            st.rerun()
        return

    # --- Sign Up Form ---
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")
    role = st.selectbox("Select Role", ["student", "educator"])
    create_account = st.button("Create Account")

    if create_account:
        existing_user = get_user(username)
        if existing_user:
            st.error("Username already exists. Please choose another one.")
            return

        if not username or not password:
            st.error("Username and password cannot be empty.")
            return

        hashed_pw = hashlib.sha256(password.encode()).hexdigest()
        create_user(username, hashed_pw, role)
        st.success("Account created! You can now log in on the Home page.")

if __name__ == "__main__":
    main()
