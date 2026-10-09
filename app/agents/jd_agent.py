from app.services.jd_generator import generate_job_description

from app.tools.job_tools import save_job

def run_jd_agent(hr_prompt: str) -> dict:
    """
    Generate and persist a job description.

    Args:
        hr_prompt: Natural-language hiring request from HR.

    Returns:
        Dictionary containing the generated JD and database ID.
    """

    job_description = generate_job_description(hr_prompt)
    job_id = save_job.invoke({"job": job_description})

    return {"job_description": job_description, "job_id": job_id}

