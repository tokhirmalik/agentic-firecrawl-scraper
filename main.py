from firecrawl import FirecrawlApp
from langgraph.graph import StateGraph
import os
from dotenv import load_dotenv

# Load .env for local testing
load_dotenv()

# API KEY
api_key = os.getenv("FIRECRAWL_API_KEY")

app = FirecrawlApp(api_key=api_key)

# Create graph
graph = StateGraph()

def scrape_step(state):
    url = state["url"]
    result = app.scrape_url(url)
    return {"result": result}

graph.add_node("scrape", scrape_step)
graph.set_entry_point("scrape")

agent = graph.compile()

if name == "__main__":
    url = "https://example.com"
    response = agent.invoke({"url": url})
    print(response)
