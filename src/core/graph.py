from langgraph.graph import StateGraph, START, END
from src.core.state import AgentState
from src.agents.agents import research_agent

workflow = StateGraph(AgentState)

# Add processing nodes
workflow.add_node("researcher", research_agent)

# Construct edge flows
workflow.add_edge(START, "researcher")
workflow.add_edge("researcher", END)

# Compile graph
compiled_agent_graph = workflow.compile()
