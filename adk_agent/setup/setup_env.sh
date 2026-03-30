#!/bin/bash

PROJECT_ID=$(gcloud config get-value project)

if [ -z "$PROJECT_ID" ]; then
  echo "❌ Set project first: gcloud config set project YOUR_PROJECT_ID"
  exit 1
fi

echo "✅ Using Project: $PROJECT_ID"

# Enable APIs
gcloud services enable aiplatform.googleapis.com
gcloud services enable bigquery.googleapis.com

# MCP enable
gcloud beta services mcp enable bigquery.googleapis.com

# Create .env
ENV_FILE="../adk_agent/mcp_finance_app/.env"

cat <<EOF > $ENV_FILE
GOOGLE_GENAI_USE_VERTEXAI=1
GOOGLE_CLOUD_PROJECT=$PROJECT_ID
GOOGLE_CLOUD_LOCATION=global
EOF

echo "✅ .env created"
