from typing import TypedDict, Annotated, Sequence
import operator

class AgentState(TypedDict):
    # Aggregates messages throughout the execution graph pipeline
    messages: Annotated[Sequence[dict], operator.add]
    current_task: str
    metrics: dict
