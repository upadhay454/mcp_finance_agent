# 💰 MCP Personal Finance Copilot

AI agent using Google ADK + MCP + BigQuery to analyze spending.

## 🚀 Features
- Spending summary
- Overspending detection
- Savings suggestions
- 600+ dummy transactions

## 🏗️ Architecture
User → Agent → MCP → BigQuery

## ⚙️ Setup

```bash
pip install -r requirements.txt
python scripts/generate_data.py

cd setup
chmod +x setup_env.sh
./setup_env.sh

chmod +x setup_bigquery.sh
./setup_bigquery.sh

adk run
