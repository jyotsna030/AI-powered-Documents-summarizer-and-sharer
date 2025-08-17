import streamlit as st
import openai
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText
from PyPDF2 import PdfReader   

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function: Generate summary using OpenAI
def generate_summary(text, instruction):
    try:
        prompt = f"{instruction}\n\nTranscript:\n{text}"
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # you can also use "gpt-4o" or "gpt-3.5-turbo"
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# Function: Send email (using Gmail SMTP)
def send_email(to_email, subject, body):
    try:
        from_email = os.getenv("SENDER_EMAIL")
        password = os.getenv("EMAIL_APP_PASSWORD")  # use App Password, not your normal password

        msg = MIMEText(body, "plain")
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = to_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())

        return "✅ Email sent successfully!"
    except Exception as e:
        return f"❌ Error sending email: {e}"

# Streamlit UI
st.title("📑 AI Meeting Notes Summarizer & Sharer")

# Upload transcript (txt or pdf)
uploaded_file = st.file_uploader("Upload Transcript (.txt or .pdf)", type=["txt", "pdf"])
custom_instruction = st.text_input("Enter your custom instruction (e.g., Summarize in bullet points):")

text = ""
if uploaded_file is not None:
    if uploaded_file.type == "application/pdf":
        # Extract text from PDF
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    else:
        # Extract text from TXT
        text = uploaded_file.read().decode("utf-8")

    if st.button("Generate Summary"):
        summary = generate_summary(text, custom_instruction)
        st.session_state["summary"] = summary

# Editable summary
if "summary" in st.session_state:
    st.subheader("📝 Editable Summary")
    edited_summary = st.text_area("Edit your summary:", st.session_state["summary"], height=300)

    # Email input
    recipient_email = st.text_input("Enter recipient email:")
    if st.button("Send Email"):
        result = send_email(recipient_email, "Meeting Notes Summary", edited_summary)
        st.success(result)
