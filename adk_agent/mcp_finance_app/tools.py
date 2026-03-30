def get_spending_summary():
    return """
    SELECT category, SUM(amount) AS total_spent
    FROM `mcp_finance.transactions`
    GROUP BY category
    ORDER BY total_spent DESC
    """

def get_overspending():
    return """
    SELECT 
        t.category,
        SUM(t.amount) AS spent,
        b.monthly_limit
    FROM `mcp_finance.transactions` t
    JOIN `mcp_finance.budgets` b
    ON t.category = b.category
    GROUP BY t.category, b.monthly_limit
    HAVING spent > b.monthly_limit
    """
