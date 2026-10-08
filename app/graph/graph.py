from langgraph.graph import END, START, StateGraph

from app.graph.jd_node import jd_node
from app.graph.state import RecruitmentState


def build_recruitment_graph():
    """
    Build the initial recruitment workflow.
    """

    graph = StateGraph(RecruitmentState)

    graph.add_node("jd_agent", jd_node)

    graph.add_edge(START, "jd_agent")
    graph.add_edge("jd_agent", END)

    return graph.compile()