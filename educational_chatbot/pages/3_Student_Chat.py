import streamlit as st
from utils.rag import create_rag_chain
from utils.database import log_chat

def main():
    st.title("Student Chat Interface")

    if "username" not in st.session_state or st.session_state.get("role") != "student":
        st.error("You must be logged in as a student to view this page.")
        st.stop()

    st.write(f"Hello, **{st.session_state['username']}** (Student).")

    if st.button("Log out"):
        del st.session_state["username"]
        del st.session_state["role"]
        st.rerun()

    if "rag_chain" not in st.session_state:
        openai_api_key = st.secrets["OPENAI_API_KEY"]
        rag_chain = create_rag_chain(
            openai_api_key=openai_api_key,
            temperature=st.session_state.get("temperature", 0.0),
            max_tokens=st.session_state.get("max_tokens", 500),
            top_k=st.session_state.get("top_k", 3),
        )
        st.session_state["rag_chain"] = rag_chain

    if "conversation_history" not in st.session_state:
        st.session_state["conversation_history"] = []

    user_question = st.text_input("Ask a question about the course materials:")
    if st.button("Send"):
        if user_question:
            # Build context from conversation history
            history_list = [
                (turn["user"], turn["bot"]) for turn in st.session_state["conversation_history"]
            ]
            result = st.session_state["rag_chain"](
                {"question": user_question, "chat_history": history_list}
            )
            answer = result["answer"]

            st.session_state["conversation_history"].append({"user": user_question, "bot": answer})
            log_chat("student", user_question, answer)

    # Display conversation
    st.write("---")
    for turn in st.session_state["conversation_history"]:
        st.write(f"**You:** {turn['user']}")
        st.write(f"**Chatbot:** {turn['bot']}")
        st.write("---")

if __name__ == "__main__":
    main()
