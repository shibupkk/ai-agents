from src.core.graph import compiled_agent_graph

if __name__ == "__main__":
    initial_state = {
        "current_task": "Analyze the impact of automated audits on GDPR compliance pipelines.",
        "messages": [],
        "metrics": {}
    }
    
    # Run the compiled orchestration pipeline
    for event in compiled_agent_graph.stream(initial_state):
        print(event)
