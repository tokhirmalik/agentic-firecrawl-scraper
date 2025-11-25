from firecrawl import FirecrawlApp
from langgraph.graph import StateGraph
import os
from dotenv import load_dotenv

# Load environment (.env)
load_dotenv()

# API KEY
api_key = os.getenv("FIRECRAWL_API_KEY")
app = FirecrawlApp(api_key=api_key)

# Create graph with dict as state
graph = StateGraph(dict)

# --- SCRAPE NODE ---
def scrape_step(state):
    url = state["url"]
    print(f"Scraping: {url}")
    result = app.scrape_url(url)
    return {"result": result}

# Add node
graph.add_node("scrape", scrape_step)
graph.set_entry_point("scrape")

# Compile agent
agent = graph.compile()

# Run script
if name == "__main__":
    test_url = "https://example.com"
    response = agent.invoke({"url": test_url})
    print("SCRAPE RESULT:", response)
