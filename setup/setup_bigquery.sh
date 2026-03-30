#!/bin/bash

PROJECT_ID=$(gcloud config get-value project)
DATASET_NAME="mcp_finance"
BUCKET_NAME="gs://mcp-finance-$PROJECT_ID"

echo "🚀 Setting up Finance Dataset..."

# Create bucket
gcloud storage buckets create $BUCKET_NAME --location=US 2>/dev/null

# Upload CSV
gcloud storage cp ../data/*.csv $BUCKET_NAME

# Create dataset
bq mk --dataset $PROJECT_ID:$DATASET_NAME 2>/dev/null

# Transactions table
bq query --use_legacy_sql=false "
CREATE OR REPLACE TABLE \`$PROJECT_ID.$DATASET_NAME.transactions\` (
    transaction_id STRING,
    date DATE,
    amount FLOAT64,
    category STRING,
    merchant STRING
);"

# Budgets table
bq query --use_legacy_sql=false "
CREATE OR REPLACE TABLE \`$PROJECT_ID.$DATASET_NAME.budgets\` (
    category STRING,
    monthly_limit FLOAT64
);"

# Load data
bq load --source_format=CSV --skip_leading_rows=1 \
$PROJECT_ID:$DATASET_NAME.transactions \
$BUCKET_NAME/transactions.csv

bq load --source_format=CSV --skip_leading_rows=1 \
$PROJECT_ID:$DATASET_NAME.budgets \
$BUCKET_NAME/budgets.csv

echo "✅ BigQuery setup complete"
