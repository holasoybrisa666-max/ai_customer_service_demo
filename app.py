import os
import json
from datetime import datetime
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv
import requests

# ==== NEW: SQLAlchemy / Postgres ====
from sqlalchemy import create_engine, Integer, String, Text, DateTime
from sqlalchemy.orm import DeclarativeBase, mapped_column, sessionmaker

# Load .env variables
load_dotenv()

# Flask app
app = Flask(__name__)

# Config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT", "You are a helpful customer service assistant.")
N8N_WEBHOOK_URL = os.getenv("N8N_WEBHOOK_URL", "")
DATABASE_URL = os.getenv("DATABASE_URL", "")

# ==== NEW: DB setup ====
engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)

class Base(DeclarativeBase):
    pass

class Conversation(Base):
    __tablename__ = "conversations"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    timestamp = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    user_message = mapped_column(Text, nullable=False)
    assistant_reply = mapped_column(Text, nullable=False)
    ip = mapped_column(String(64))
    user_agent = mapped_column(Text)

SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)

# 自动建表（第一次运行会创建）
Base.metadata.create_all(engine)

# OpenAI client (new SDK)
try:
    from openai import OpenAI
    oai_client = OpenAI()
except Exception:
    oai_client = None


def call_openai(message: str) -> str:
    if not oai_client:
        return "OpenAI SDK not available on server."
    try:
        completion = oai_client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message},
            ],
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"[Error calling OpenAI: {e}]"

def log_to_n8n(payload: dict):
    if not N8N_WEBHOOK_URL:
        return
    try:
        requests.post(N8N_WEBHOOK_URL, json=payload, timeout=5)
    except Exception:
        pass

def log_to_file(payload: dict):
    # 确保 logs 目录存在
    os.makedirs("logs", exist_ok=True)
    path = os.path.join("logs", "conversations.jsonl")
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")

# ==== NEW: 写入数据库 ====
def log_to_db(payload: dict):
    try:
        with SessionLocal() as s:
            s.add(Conversation(
                user_message=payload.get("user_message", ""),
                assistant_reply=payload.get("assistant_reply", ""),
                ip=payload.get("meta", {}).get("ip"),
                user_agent=payload.get("meta", {}).get("user_agent"),
            ))
            s.commit()
    except Exception as e:
        print(f"[DB log failed] {e}")


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = (data.get("message") or "").strip()
    if not user_message:
        return jsonify({"error": "message is required"}), 400

    reply = call_openai(user_message)

    record = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "user_message": user_message,
        "assistant_reply": reply,
        "meta": {
            "ip": request.headers.get("X-Forwarded-For", request.remote_addr),
            "user_agent": request.headers.get("User-Agent"),
        },
    }
    # log
    log_to_file(record)
    log_to_n8n(record)
    log_to_db(record)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
