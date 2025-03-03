# RAG-Powered AI Chatbot for Education

## 📖 Overview
This project is a **Retrieval-Augmented Generation (RAG) chatbot** designed for educators and students. Educators can upload **various file types**, which are processed and stored in a **NeonDB (PostgreSQL) database** with **pgvector**. Students can interact with a **GPT-4-powered chatbot**, which retrieves relevant information from the uploaded materials to provide **context-aware responses**.

---

## ✨ Features
### 🎓 Educator Dashboard
- 📂 Upload multiple file types: **TXT, CSV, Markdown, PDF, Word (DOCX), and Excel (XLSX, XLS)**.
- 🔍 Convert documents into **vector embeddings** stored in NeonDB.
- ⚙️ Configure chatbot parameters (retrieval size, temperature, max tokens).
- 📜 Review and manage **student chat logs**.

### 💬 Student Chatbot
- 🧠 Interact with a **GPT-4-powered AI assistant**.
- 📖 Retrieves relevant information from uploaded materials.
- 📊 Chat history is **logged for educators**.

### 🔐 Authentication & Security
- 👨‍🏫 **Educators** can upload materials & review logs.
- 👩‍🎓 **Students** can only chat with the AI assistant.
- 🔒 Secure **username & password storage** in NeonDB.

---

## 🛠 Installation Guide
### ✅ Prerequisites
Before installing, ensure you have:
- **Python 3.8+** ([Download here](https://www.python.org/downloads/))
- **pip** (comes with Python)
- **A NeonDB (PostgreSQL) account** ([Sign up here](https://neon.tech/))

### 🔽 Clone the Repository
Download the project to your local machine:
```bash
git clone https://github.com/YOUR_USERNAME/RAG-AI-Chatbot.git
cd RAG-AI-Chatbot
```

### 🏗 Create a Virtual Environment
Set up a Python virtual environment:
```bash
python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate  # On Windows
```

### 📦 Install Dependencies
Run the following command to install required packages:
```bash
pip install -r requirements.txt
```
This will install:
- **Streamlit** (UI framework)
- **LangChain** (AI framework)
- **OpenAI GPT-4 API**
- **PostgreSQL client (`psycopg2`)**
- **pgvector for vector search (`langchain_postgres`)**
- **pandas, pdfplumber, python-docx** (for file processing)

---

## 🗄 Setting Up the Database (NeonDB)
### 🌐 Create a NeonDB Account
1. **Go to** [NeonDB](https://neon.tech/) and create an account.
2. **Create a new database**.
3. **Copy the connection string**, which will look like:
   ```
   postgresql://your_username:your_password@your-neon-instance.neon.tech/your_db?sslmode=require
   ```

### 🔑 Store Database Credentials
1. Create a **`.streamlit` directory** (if it doesn’t exist).
2. Inside `.streamlit/`, create a file called **`secrets.toml`**.
3. Add your credentials:
   ```toml
   OPENAI_API_KEY = "your-openai-api-key"
   NEONDB_CONNECTION_STRING = "postgresql://your_username:your_password@your-neon-instance.neon.tech/your_db?sslmode=require"
   ```

### ⚙️ Initialize the Database
Run the following commands to set up the necessary tables:
```bash
python -c "from utils.database import init_db; init_db()"
python -c "from utils.rag import init_rag_db; init_rag_db()"
```
This will:
✔️ Enable **pgvector** extension  
✔️ Create **users** table (for authentication)  
✔️ Create **chat logs** table  
✔️ Create **embeddings** table (for storing document vectors)  

---
🛠 Deployment on Streamlit Cloud

✅ Prerequisites

Before deploying, ensure you have:

A GitHub repository with this project.

A Streamlit Cloud account (Sign up here).

A NeonDB (PostgreSQL) account (Sign up here).

🚀 Steps to Deploy

Push Your Project to GitHub

git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/RAG-AI-Chatbot.git
git push -u origin main

Go to Streamlit Cloud (Streamlit Cloud)

Create a New App:

Select your GitHub repository.

Choose Home.py as the main file.

Click Deploy.

Set Environment Variables in Streamlit Cloud:

Open the Secrets Manager in the Streamlit Cloud settings.

Add the following secrets:

OPENAI_API_KEY = "your-openai-api-key"
NEONDB_CONNECTION_STRING = "postgresql://your_username:your_password@your-neon-instance.neon.tech/your_db?sslmode=require"

Click Save.

Restart Your Streamlit Cloud App

Your app should now be live with a URL like:

https://your-username-your-app.streamlit.app

---
## ▶️ Running the Application
Start the app by running:
```bash
streamlit run Home.py
```

### 🎮 Using the App
1. **Log in or sign up**:
   - **Educators** can upload files & review chat logs.
   - **Students** can chat with the AI assistant.
2. **Educators**:
   - Upload documents to store them in **NeonDB**.
   - Set chatbot parameters (retrieval size, temperature, max tokens).
   - Review **student interactions**.
3. **Students**:
   - Ask questions and get AI-generated answers based on uploaded content.
   - The chatbot will fetch **relevant information** from the stored documents.

---

## ⚠️ Troubleshooting
### ❌ "Cannot Import OpenAIEmbeddings"
Run:
```bash
pip install --upgrade langchain langchain_openai langchain_postgres psycopg2 pandas pdfplumber python-docx
```

### ❌ Database Connection Error
Ensure:
- Your **NeonDB connection string** in `secrets.toml` is **correct**.
- Your **NeonDB user & password** are valid.
- Your **Neon instance is running**.

### ❌ No Chatbot Responses
- Check that **files have been uploaded**.
- Ensure **OpenAI API key** is **valid** in `secrets.toml`.

---

## 📂 File Structure
```
RAG-AI-Chatbot/
├── Home.py                # Login Page
├── .streamlit/
│   ├── secrets.toml       # Stores API keys & database credentials
├── pages/
│   ├── 1_SignUp.py        # Sign-Up Page
│   ├── 2_Educator_Dashboard.py  # Educator View
│   ├── 3_Student_Chat.py  # Chatbot for students
├── utils/
│   ├── database.py        # Handles user authentication & chat logs
│   ├── rag.py             # Handles RAG storage & retrieval
├── requirements.txt       # Dependencies
└── README.md              # This guide
```
---

🔹 **If this project helps you, please ⭐ the repository!**  

---

## ⭐ Enjoy Building with AI & RAG!
This project is designed for **educators** who want to integrate **AI-powered** chat experiences using **retrieval-augmented generation** (RAG). 🚀

