from firecrawl import FirecrawlApp
from langgraph.graph import StateGraph
from typing import TypedDict
import os
from dotenv import load_dotenv

load_dotenv()

# FIRECRAWL API KEY
api_key = os.getenv("FIRECRAWL_API_KEY")
app = FirecrawlApp(api_key=api_key)

# STATE SCHEMA
class ScrapeState(TypedDict):
    url: str
    result: dict | None

# CREATE GRAPH
graph = StateGraph(ScrapeState)

def scrape_step(state: ScrapeState) -> ScrapeState:
    url = state["url"]

    # OLD: result = app.scrape_url(url)
    result = app.scrape(url=url)   # ✅ TO‘G‘RI METOD

    return {"url": url, "result": result}

graph.add_node("scrape", scrape_step)
graph.set_entry_point("scrape")

agent = graph.compile()

if __name__ == "__main__":
    response = agent.invoke({"url": "https://example.com", "result": None})
    print(response)
