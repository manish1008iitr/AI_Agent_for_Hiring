from app.agents.jd_agent import run_jd_agent
from app.graph.state import RecruitmentState


def jd_node(state: RecruitmentState) -> RecruitmentState:
    """
    LangGraph node responsible for generating and saving a job description.
    """

    hr_prompt = state["hr_prompt"]

    result = run_jd_agent(hr_prompt)

    return {
        **state,
        "job_id": result["job_id"],
        "job_description": result["job_description"],
        "status": "job_created",
    }