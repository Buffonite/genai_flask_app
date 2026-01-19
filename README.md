# 🧠 GenAI Flask App  
A fully deployed AI web application built with **Flask**, **IBM Watsonx**, and **LangChain**, supporting multiple LLMs including **Llama**, **Granite**, and **Mistral**.

🔗 **Live Demo:** https://genai-flask-app-1.onrender.com  
*(Hosted on Render — publicly accessible)*

---

## 🚀 Overview

GenAI Flask App is a full‑stack AI assistant demonstrating real-world AI engineering:

- 🌐 Interactive web UI (HTML + JavaScript)
- 🧩 Flask backend with REST API
- 🤖 Multi‑model support (Llama / Granite / Mistral)
- 🧠 LangChain prompt templates + JSON output parsing
- 🔐 Secure environment variable handling
- ☁️ Fully deployed and live on Render

This project showcases how to build, integrate, and deploy modern LLM applications end‑to‑end.

---

## 🛠️ Tech Stack

### **Backend**
- Python 3.10+
- Flask
- LangChain
- IBM Watsonx AI SDK

### **Frontend**
- HTML / CSS / JavaScript
- Fetch API

### **Deployment**
- Render Web Service
- GitHub for version control
- Environment variables for secrets

---

## 📁 Project Structure

```
genai_flask_app/
│── app.py                # Flask backend API
│── model.py              # Model logic (Llama/Granite/Mistral)
│── templates/
│     └── index.html      # Frontend UI
│── static/
│     └── script.js       # Frontend logic
│── requirements.txt      # Dependencies
│── README.md             # Documentation
```

---

## 🤖 Features

### **Multi‑Model AI Assistant**
Users can switch between:
- **Llama**
- **Granite**
- **Mistral**

Each model is wrapped with LangChain and returns structured JSON output.

### **Unified Response Format**
All models return:

```json
{
  "response": "Model output here",
  "duration": 0.53
}
```

### **Secure API Handling**
No API keys are hard‑coded.  
All secrets are stored in environment variables.

### **Cloud Deployment**
The app is fully deployed and accessible online.

---

## 🧠 Future Enhancements

- Multi‑turn conversation memory  
- Chat history storage  
- User authentication  
- Token usage tracking  
- Improved UI/UX  
- Custom domain  
- Database integration  
- Parallel model inference  

---

## 📜 License

MIT License

---

## ✨ Author

**barry**  
AI developer passionate about building real, deployable AI applications.

