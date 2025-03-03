import streamlit as st
from utils.database import fetch_chat_logs
from utils.rag import convert_files_to_docs, store_embeddings_in_neon

def main():
    st.title("Educator Dashboard")

    # Ensure only educators can access this page
    if "username" not in st.session_state or st.session_state.get("role") != "educator":
        st.error("You must be logged in as an educator to view this page.")
        st.stop()

    st.write(f"Hello, **{st.session_state['username']}** (Educator).")

    # Log out button
    if st.button("Log out"):
        del st.session_state["username"]
        del st.session_state["role"]
        st.experimental_rerun()

    # File Upload Section
    st.write("Upload multiple files for the knowledge base.")
    uploaded_files = st.file_uploader(
        "Upload Files", accept_multiple_files=True, 
        type=["txt", "md", "csv", "pdf", "docx", "xlsx", "xls"]
    )

    # Chatbot Configuration Options
    top_k = st.slider("Top-K retrieval", min_value=1, max_value=10, value=3)
    temperature = st.slider("LLM Temperature", min_value=0.0, max_value=1.0, value=0.0)
    max_tokens = st.slider("Max Tokens", min_value=100, max_value=2000, value=500)
    system_prompt = st.text_area("System Prompt", value="You are a helpful teaching assistant.")

    build_button = st.button("Build/Update Knowledge Base")

    # Process uploaded files and store embeddings
    if build_button and uploaded_files:
        with st.spinner("Building vector database..."):
            st.session_state["system_prompt"] = system_prompt
            st.session_state["top_k"] = top_k
            st.session_state["temperature"] = temperature
            st.session_state["max_tokens"] = max_tokens

            # Convert files into documents and store in vector database
            docs = convert_files_to_docs(uploaded_files)
            store_embeddings_in_neon(docs)

            st.success("Knowledge base updated successfully!")

    # Display Chat Logs
    st.write("---")
    st.subheader("Chat Logs")
    if st.button("Refresh Logs"):
        logs = fetch_chat_logs()
        if logs:
            for row in logs:
                log_id, role, user_message, bot_response, timestamp = row
                st.markdown(f"**[{timestamp}]** **{role}** asked:")
                st.markdown(f"> **User:** {user_message}")
                st.markdown(f"> **Bot:** {bot_response}")
                st.write("---")
        else:
            st.info("No chat logs found.")

if __name__ == "__main__":
    main()
