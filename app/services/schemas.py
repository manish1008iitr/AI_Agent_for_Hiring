from pydantic import BaseModel, Field
from typing import List, Optional, Literal

class JobDescription(BaseModel):

    title: str = Field(description = "title of the job")

    summary: str = Field(description = "Short summary of the the job ")

    responsibilities: List[str] = Field(description = "Main responsibilites of the job")

    must_have_skills: List[str] = Field(description = "mandatory skills that a candidate must have for the job")

    nice_to_have_skills: List[str] = Field(description= "Preferred but non-mandatory skills")

    minimum_experience_years: Optional[float] = Field(
        default = None,
        description = "Minimum years of relevant experience"
    )

    education: List[str] = Field(
        default_factory=list,
        description="Required or preferred educational qualifications"
    )

    location: Optional[str] = Field(
        default = None, 
        description = "Job location or work mode"
    )

    employment_type: Optional[str] = Field(
        default=None,
        description="Full-time, part-time, contract, etc."
    )

    salary_range: Optional[str] = Field(
        default = None, 
        description = "Range of the salary for the job"
    )


class SkillAssessment(BaseModel):
    skill: str = Field(description="Skill required by the job")
    status: Literal["demonstrated","partially_demonstrated","not_found",] = Field(description="How well the resume evidence supports this skill")
    evidence: str = Field(description="Supporting resume evidence, or explain that no evidence was found")


class CandidateScreeningResult(BaseModel):
    candidate_id: str = Field(description="Unique candidate identifier")

    overall_fit_score: int = Field(
        ge=0,
        le=100,
        description="Evidence-based alignment score against the job requirements",
    )

    must_have_assessments: list[SkillAssessment] = Field(
        description="Assessment of every mandatory job skill"
    )

    nice_to_have_assessments: list[SkillAssessment] = Field(
        description="Assessment of preferred job skills"
    )

    relevant_experience_summary: str = Field(
        description="Summary of relevant experience demonstrated in the resume"
    )

    strengths: list[str] = Field(
        description="Evidence-backed strengths relevant to the role"
    )

    gaps: list[str] = Field(
        description="Missing evidence, partial matches, or relevant experience gaps"
    )

    recommendation: Literal[
        "strong_match",
        "possible_match",
        "insufficient_evidence",
    ] = Field(
        description="Suggested level of HR review, not a hiring decision"
    )

    rationale: str = Field(
        description="Concise explanation of the assessment based on resume evidence"
    )