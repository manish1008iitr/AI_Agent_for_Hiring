from typing import TypedDict, Literal, List, Dict, Optional, Any

class RecruitmentState(TypedDict, total=False):
    # Original HR request

    """
    Shared state for the recruitment workflow.
    """
    
    # Original request from HR
    hr_prompt: str

    # Generated job description
    job_description: Any

    # Database ID of the job
    job_id: int

    # Candidate/resume information will be added later
    candidates: list

    # Screening results will be added later
    screening_results: list

    # Interview information will be added later
    interview_details: dict

    # Communication information will be added later
    communication_details: dict

    # Human approval information
    human_approval: dict

    # General workflow status
    status: str

    # Errors encountered during workflow
    error: str
