
#  AI Customer Service Assistant

An intelligent customer service chatbot built with **Flask + OpenAI + PostgreSQL**, featuring database logging, n8n webhook automation, and a clean web interface.

---

## Features

- AI-powered chat using OpenAI GPT-4o-mini
- Automatic logging of all conversations to PostgreSQL
- Simple web admin interface for viewing logs
- Integration with n8n workflows via webhook
- Configurable with `.env` environment file
- Built with Flask, easy to deploy on Render or Railway

---

## Tech Stack

| Layer | Technology |
|--------|-------------|
| Backend | Flask (Python) |
| AI Model | OpenAI GPT-4o-mini |
| Database | PostgreSQL + SQLAlchemy ORM |
| Automation | n8n Webhook Integration |
| Frontend | HTML + CSS + JavaScript (Flask templates) |

---

## How to Run Locally

```bash
git clone https://github.com/yourname/ai_customer_service_demo.git
cd ai_customer_service_demo

python -m venv .venv
.\.venv\Scripts\Activate.ps1  # For Windows PowerShell
pip install -r requirements.txt

# Create your environment file
copy .env.example .env
# Edit .env with your own API keys and database URL

python app.py
```

Then open: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Demo Screenshots

### Project Running (Flask)
![Run Server](static/run_server.png)

### Chat Interface
![Chat Demo](static/chat_demo.png)

### Database Logs (PostgreSQL)
![Database Logs](static/db_logs.png)

### n8n Workflow Integration
![n8n Workflow](static/n8n_workflow.png)

### n8n Execution Log
![n8n Execution](static/n8n_execution.png)

### Project Structure
![Project Structure](static/project_structure.png)

---

## ⚙️ Environment Variables (.env)

```bash
# OpenAI API Key
OPENAI_API_KEY=sk-xxxxx

# Flask
FLASK_ENV=development
SECRET_KEY=your-secret-key

# PostgreSQL Database
DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@localhost:5432/DB_NAME


---

## Future Improvements

- Add FAQ knowledge base for smarter contextual replies  
- Implement role-based admin dashboard  
- Integrate analytics for chat insights  

---

##  Author

**Ting Liu** — AI Developer & Automation Enthusiast  
 Email: [holasoybrisa666@gmail.com](mailto:holasoybrisa666@gmail.com)  

---

⭐ *If you like this project, consider starring it on GitHub!* ⭐
