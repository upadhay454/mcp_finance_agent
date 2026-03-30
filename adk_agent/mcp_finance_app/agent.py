import google.auth
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

# Auth
credentials, project_id = google.auth.default(
    scopes=["https://www.googleapis.com/auth/bigquery"]
)

credentials.refresh(google.auth.transport.requests.Request())
token = credentials.token

# MCP BigQuery
bq_toolset = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url="https://bigquery.googleapis.com/mcp",
        headers={
            "Authorization": f"Bearer {token}",
            "x-goog-user-project": project_id,
        },
    )
)

# Agent
root_agent = LlmAgent(
    model="gemini-3-pro-preview",
    name="finance_agent",
    instruction="""
    You are a Personal Finance Assistant.

    Help users:
    - Analyze spending
    - Detect overspending
    - Suggest savings

    Use BigQuery MCP tools to query:
    - transactions
    - budgets

    Always provide clear insights.
    """,
    tools=[bq_toolset],
)
