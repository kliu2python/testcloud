# TestCloud

A web-based automated testing dashboard for FortiGate & FortiAuthenticator QA.  
Built with **FastAPI + React + PostgreSQL + Redis + vLLM**.

---

## 🚀 Quick Start

### 1. Run the generator
```bash
chmod +x setup.sh
./setup.sh

### 2. Start containers
docker-compose up -d --build

### 3. Access UI

Frontend: http://localhost:5173

Backend: http://localhost:8000

🔌 Features
✔ VM Dashboard

View FortiGate/FortiAuthenticator VM test status

Test priority

Pass/Fail aggregation

✔ Device Dashboard

Pull device info directly from MCloud/STF API

Show iOS/Android/macOS/VM availability

✔ AI Test Analysis

Sends prompt to vLLM/OpenAI-compatible endpoint

Useful for test code analysis or result summarization

✔ File Manager

Upload .apk, .ipa, .zip, .yaml, .py test bundles

View uploaded test files

⚙️ Environment Variables

Create backend/.env based on backend/.env.example:

MCLOUD_API_BASE=http://10.160.13.118/api/v1
MCLOUD_TOKEN=<your token>

LLM_API_BASE=http://your-vllm-server/v1
LLM_API_KEY=<your key>
LLM_MODEL=qwen2.5-32b-instruct

🧱 Architecture
testcloud/
├── backend/    # FastAPI + PostgreSQL + Redis
├── frontend/   # React dashboard
├── docker-compose.yml
└── README.md

🐳 Containers
Service	Port	Description
backend	8000	FastAPI API server
frontend	5173	React dashboard
postgres	5432	TestCloud DB
redis	6379	async job coordination
📌 Notes

backend/uploads is mounted automatically

real STF/MCloud API used for device listing

AI analysis works with vLLM or OpenAI-style endpoint

