from firecrawl import FirecrawlApp
from langgraph.graph import StateGraph
from pydantic import BaseModel
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Firecrawl API key
api_key = os.getenv("FIRECRAWL_API_KEY")
app = FirecrawlApp(api_key=api_key)

# --- STATE SCHEMA ---
class ScrapeState(BaseModel):
    url: str
    result: dict | None = None

# Graph yaratish
graph = StateGraph(ScrapeState)

# Scrape-step
def scrape_step(state: ScrapeState):
    result = app.scrape_url(state.url)
    return {"result": result}

graph.add_node("scrape", scrape_step)
graph.set_entry_point("scrape")

agent = graph.compile()

# --- RUN ---
if name == "__main__":
    response = agent.invoke({"url": "https://example.com"})
    print(response)
