
# 🤖 AI 客服系统

一个基于 **Flask + OpenAI + PostgreSQL** 构建的智能客服聊天系统，
支持自动对话记录、n8n 自动化集成，并拥有简洁直观的网页界面。

---

## 🌟 功能亮点

- 💬 基于 OpenAI GPT-4o-mini 的 AI 聊天功能  
- 🗂 自动将每次对话保存至 PostgreSQL 数据库  
- 📊 提供后台管理界面，可查看和导出聊天记录  
- 🔗 集成 n8n Webhook，实现自动化工作流  
- ⚙️ 使用 `.env` 文件进行环境配置  
- 🧱 结构清晰，支持部署到 Render / Railway 等云平台  

---

## 🛠 技术栈

| 模块 | 技术 |
|------|------|
| 后端 | Flask (Python) |
| AI 模型 | OpenAI GPT-4o-mini |
| 数据库 | PostgreSQL + SQLAlchemy ORM |
| 自动化 | n8n Webhook 集成 |
| 前端 | HTML + CSS + JavaScript (Flask 模板) |

---

## 🚀 本地运行步骤

```bash
git clone https://github.com/yourname/ai_customer_service_demo.git
cd ai_customer_service_demo

python -m venv .venv
.\.venv\Scripts\Activate.ps1  # Windows PowerShell 激活虚拟环境
pip install -r requirements.txt

# 创建环境配置文件
copy .env.example .env
# 在 .env 文件中填写你的 API Key 和数据库连接信息

python app.py
```

运行后打开浏览器访问：  
👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📸 项目截图

### 💻 Flask 运行界面
![Run Server](static/run_server.png)

### 💬 聊天页面
![Chat Demo](static/chat_demo.png)

### 🗄️ 数据库存储（PostgreSQL）
![Database Logs](static/db_logs.png)

### 🔗 n8n 工作流集成
![n8n Workflow](static/n8n_workflow.png)

### ⚙️ n8n 执行日志
![n8n Execution](static/n8n_execution.png)

### 📁 项目结构
![Project Structure](static/project_structure.png)

---

## ⚙️ 环境变量 (.env)

```bash
# OpenAI API Key
OPENAI_API_KEY=sk-xxxxx

# Flask 设置
FLASK_ENV=development
SECRET_KEY=your-secret-key

# PostgreSQL 数据库连接
DATABASE_URL=postgresql+psycopg2://USER:PASSWORD@localhost:5432/DB_NAME

# n8n Webhook (可选)
N8N_WEBHOOK_URL=https://your-n8n-url/webhook/ai_logs
```

---

## 🧠 后续可扩展方向

- 增加 FAQ 知识库，实现基于上下文的智能问答  
- 开发带权限控制的后台管理系统  
- 增加聊天数据分析与统计功能  

---

## 🧑‍💻 作者

**Ting Liu** — AI 开发者 & 自动化爱好者  
🌐 个人主页：[yourportfolio.com](https://yourportfolio.com)  
📧 邮箱：[your@email.com](mailto:your@email.com)  

---

⭐ *如果你喜欢这个项目，欢迎在 GitHub 点个 Star！* ⭐
