from pydantic import BaseModel, Field
from typing import List, Optional

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


