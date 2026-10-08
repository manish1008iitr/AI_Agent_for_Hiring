from typing import Optional, List

from pydantic import BaseModel, Field


class EmploymentBlock(BaseModel):
    """
    Represents one employment experience from a resume.
    """

    block_id: str

    candidate_id: str

    role: Optional[str] = None

    company: Optional[str] = None

    start_date: Optional[str] = None

    end_date: Optional[str] = None

    description: str = ""

    metadata: dict = Field(
        default_factory=dict
    )

class EmploymentExtraction(BaseModel):
    """
    Collection of employment experiences extracted
    from a resume.
    """

    employments: List[EmploymentBlock]
