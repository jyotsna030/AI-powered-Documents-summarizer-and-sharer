
# 📑 AI-Powered Meeting Notes Summarizer & Sharer

An end-to-end **full-stack application** that allows users to upload meeting transcripts (TXT/PDF), generate AI-powered summaries with custom instructions, edit them, and share them via email.  

---

## 🚀 Project Overview

This project was built as part of an assignment to create a **full-stack AI application** focusing on functionality.  

### **Features**
- Upload transcripts in **.txt** or **.pdf** format  
- Provide a **custom instruction/prompt** (e.g., "Summarize in bullet points" or "Highlight only action items")  
- Get an AI-generated summary using **OpenAI API**  
- Edit the summary inside the app before finalizing  
- Share the final summary via **email**  
- Simple, functional UI powered by **Streamlit**  

---

## 🛠️ Tech Stack

### **Frontend**
- [Streamlit](https://streamlit.io/) → for a simple, fast UI

### **Backend**
- [Python](https://www.python.org/)  
- [OpenAI API](https://platform.openai.com/) → for AI summarization  
- [PyPDF2](https://pypi.org/project/PyPDF2/) → for PDF text extraction  
- [smtplib](https://docs.python.org/3/library/smtplib.html) → for email functionality  

### **Deployment**
- [GitHub](https://github.com/) → version control  
- [Streamlit Cloud](https://streamlit.io/cloud) → app hosting  
- Secrets handled securely via **Streamlit Secrets Manager**  

---

## 📂 Project Structure

```

├── app.py            # Main Streamlit app
├── .gitignore        # Ensures .env and secrets aren’t pushed
├── README.md         # Project documentation
└── requirements.txt  # Dependencies

````

---

## 🔑 How It Works

1. **Upload Transcript** → TXT or PDF file  
2. **Enter Instruction** → e.g. "Give me a 3-line summary"  
3. **Generate Summary** → OpenAI API processes the text  
4. **Edit Summary** → Make final modifications inside the app  
5. **Share Summary** → Enter recipient email and send  

---

## 📊 Flowchart

![Flowchart](https://github.com/jyotsna030/AI-powered-Documents-summarizer-and-sharer/blob/main/AI-Docs-summarizer.png)  


---

## 🎥 Demo Video

[![Watch the Demo](https://img.youtube.com/vi/your-demo-video-id/0.jpg)](https://www.youtube.com/watch?v=your-demo-video-id)  
*(Replace with your YouTube demo link once recorded)*  

---

## 📌 Approach

- **Step 1:** Chose **Streamlit** for simplicity → avoids heavy frontend code.  
- **Step 2:** Integrated **OpenAI API** for flexible summarization.  
- **Step 3:** Used **PyPDF2** to allow PDF input along with text files.  
- **Step 4:** Added an **editable text area** for users to refine summaries.  
- **Step 5:** Integrated **SMTP email sending** with secure **App Passwords**.  
- **Step 6:** Deployed app on **Streamlit Cloud**, keeping secrets safe in **Secrets Manager**.  

---

## 🌱 Future Enhancements

- Add **authentication** (login system)  
- Store past meeting summaries in a **database (Postgres/SQLite)**  
- Export summaries in **PDF/Word** formats  
- Add **multi-language support**  
- Support for **audio transcription** (upload MP3/WAV → auto-convert to text → summarize)  

---

## ⚡ Getting Started

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/your-username/AI-powered-meeting-notes-summarizer-and-sharer.git
cd AI-powered-meeting-notes-summarizer-and-sharer
````

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run Locally

```bash
streamlit run app.py
```

### 4️⃣ Set Up Secrets

In Streamlit Cloud → **App → Settings → Secrets Manager**:

```toml
OPENAI_API_KEY = "your-openai-api-key"
SENDER_EMAIL = "your-email@gmail.com"
EMAIL_APP_PASSWORD = "your-app-password"
```

