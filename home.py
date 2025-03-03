import streamlit as st
import hashlib
from utils.database import init_db, get_user

def main():
    st.set_page_config(page_title="RAG Chatbot - Login", layout="wide")
    init_db()  # Create user/chat tables if they don't exist

    st.title("Login")

    # If user is already logged in, show a simple message and logout
    if "username" in st.session_state:
        st.write(f"You are already logged in as: **{st.session_state['username']}**")
        if st.button("Log out"):
            del st.session_state["username"]
            del st.session_state["role"]
            st.rerun()
        return

    # --- Login Form ---
    st.subheader("Please log in")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    login_button = st.button("Login")

    if login_button:
        # Check if user exists
        user = get_user(username)
        if user:
            user_id, db_username, db_password, db_role, _ = user
            # Hash the entered password
            hashed_input_pw = hashlib.sha256(password.encode()).hexdigest()
            if hashed_input_pw == db_password:
                # Successful login
                st.session_state["username"] = db_username
                st.session_state["role"] = db_role
                st.success(f"Logged in as {db_role}!")
            else:
                st.error("Incorrect password. Please try again.")
        else:
            st.error("User not found. Please try again or sign up.")

    st.write("New user? Go to **SignUp** in the sidebar to create an account.")

if __name__ == "__main__":
    main()
