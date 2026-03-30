import csv
import random
from datetime import datetime, timedelta

categories = ["Food", "Transport", "Shopping", "Bills", "Entertainment"]

merchants = {
    "Food": ["Swiggy", "Zomato", "Dominos"],
    "Transport": ["Uber", "Ola"],
    "Shopping": ["Amazon", "Flipkart"],
    "Bills": ["Electricity", "Internet"],
    "Entertainment": ["Netflix", "Spotify"]
}

start_date = datetime(2026, 1, 1)

with open("../data/transactions.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["transaction_id", "date", "amount", "category", "merchant"])

    for i in range(600):
        category = random.choice(categories)
        merchant = random.choice(merchants[category])
        date = start_date + timedelta(days=random.randint(0, 90))
        amount = random.randint(100, 3000)

        writer.writerow([i, date.strftime("%Y-%m-%d"), amount, category, merchant])

print("✅ transactions.csv created")

# budgets
with open("../data/budgets.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["category", "monthly_limit"])

    writer.writerow(["Food", 6000])
    writer.writerow(["Transport", 4000])
    writer.writerow(["Shopping", 7000])
    writer.writerow(["Bills", 10000])
    writer.writerow(["Entertainment", 3000])

print("✅ budgets.csv created")
