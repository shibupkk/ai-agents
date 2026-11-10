import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from src.core.state import AgentState

load_dotenv()
# Initialize your LLM engine
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

def research_agent(state: AgentState):
    """An agent node that handles data extraction or querying APIs."""
    print("--- RUNNING RESEARCH AGENT ---")
    response = llm.invoke(f"Research the following task: {state['current_task']}")
    return {"messages": [{"role": "assistant", "content": response.content}]}
