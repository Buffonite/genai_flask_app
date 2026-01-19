# 🧠 GenAI Flask App  
A lightweight yet production‑ready AI web application built with **Flask**, **IBM Watsonx**, and **LangChain**, supporting multiple LLMs including **Llama**, **Granite**, and **Mistral**.

This project demonstrates full‑stack AI engineering: model orchestration, prompt templating, JSON‑structured outputs, and cloud deployment.

---

## 🚀 Overview

GenAI Flask App is a complete end‑to‑end AI assistant featuring:

- 🌐 A clean web interface (HTML + JavaScript)
- 🧩 A Flask backend with REST API endpoints
- 🤖 Multi‑model support (Llama / Granite / Mistral)
- 🧠 LangChain prompt templates + JSON output parsing
- 🔐 Secure environment variable handling (no hard‑coded keys)
- ☁️ Deployment on Render with public access

It’s designed as a practical, real‑world AI application suitable for learning, showcasing, or extending into a larger product.

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
│── README.md             # Project documentation
```

---

## 🔧 Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/Buffonite/genai_flask_app
cd genai_flask_app
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set environment variables
```
WATSONX_API_KEY=your_api_key
WATSONX_PROJECT_ID=your_project_id
```

### 4. Start the server
```bash
python app.py
```

Visit:

```
http://localhost:5000
```

---

## ☁️ Deploying to Render

1. Push the project to GitHub  
2. Create a new **Render Web Service**  
3. Configure:

**Build Command**
```
pip install -r requirements.txt
```

**Start Command**
```
python app.py
```

4. Add environment variables:

```
WATSONX_API_KEY=xxxx
WATSONX_PROJECT_ID=xxxx
```

5. Deploy and access your public URL.

---

## 🤖 Model Selection

The frontend sends:

```json
{
  "model": "llama",
  "user_message": "Hello"
}
```

The backend routes the request to the selected model and returns a unified response:

```json
{
  "response": "Model output here",
  "duration": 0.53
}
```

Supported models:

- `llama`
- `granite`
- `mistral`

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

**Barry**  
A hands‑on AI developer passionate about building real, deployable AI applications.
