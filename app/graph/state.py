from typing import TypedDict, Literal, List, Dict, Optional, Any

class RecruitmentState(TypedDict, total=False):
    # Original HR request
    user_request: str

    # Workflow identification
    workflow_id: str
    job_id: Optional[int]

    # Job information
    job_description: Dict[str, Any]

    # Resume information
    resume_ids: List[int]
    candidates: List[Dict[str, Any]]

    # Screening
    shortlisted_candidates: List[Dict[str, Any]]

    # Interview
    interview_slots: List[Dict[str, Any]]
    selected_slots: Dict[int, Dict[str, Any]]

    # Communication
    communications: List[Dict[str, Any]]

     # Human approval
    pending_approval: Optional[Dict[str, Any]]
    human_decision: Optional[str]

    # Agent control
    current_agent: Optional[str]
    next_action: Optional[str]

    # Errors
    errors: List[str]

    # Conversation
    conversation_id: Optional[str]

