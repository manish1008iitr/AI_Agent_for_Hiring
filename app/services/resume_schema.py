from typing import List

from pydantic import BaseModel, Field


class ResumeSection(BaseModel):
    """
    A logical section extracted from a resume.
    """

    section_name: str = Field(
        description="Name of the resume section"
    )

    content: str = Field(
        description="Text contained in the section"
    )


class ProcessedResume(BaseModel):
    """
    Structured representation of a processed resume.
    """

    candidate_id: str = Field(
        description="Unique identifier for the candidate"
    )

    file_name: str = Field(
        description="Original resume file name"
    )

    raw_text: str = Field(
        description="Complete extracted resume text"
    )

    sections: List[ResumeSection] = Field(
        default_factory=list,
        description="Logical sections extracted from the resume"
    )