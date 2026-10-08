from typing import List

from langchain_core.prompts import ChatPromptTemplate

from app.services.employment_schema import (
        EmploymentBlock, 
        EmploymentExtraction
    )
from app.services.llm import get_llm

def extract_employment_blocks(candidate_id: str, experience_text: str,) -> List[EmploymentBlock]:
    """
    Extract individual employment records from
    the Experience section of a resume.
    """

    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages(
        [("system", """
            You are an expert resume parser.

            Extract individual employment experiences
            from the provided resume experience section.

            For each employment:

            - Identify the job role.
            - Identify the company.
            - Identify the start date if available.
            - Identify the end date if available.
            - Preserve the responsibilities and achievements belonging to that employment.
            - Do not invent information.
            - If information is missing, return null.
            - Keep each employment description coherent.
            - Do not generate block_id. Leave block_id empty.

            Return the employment records in the requested
            structured format.
            """),
            ("human","""
        Candidate ID:

        {candidate_id}

        Experience section:

        {experience_text}
        """),
        ]
    )

    structured_llm = llm.with_structured_output(
        EmploymentExtraction
    )

    chain = prompt | structured_llm

    result = chain.invoke(
        {
            "candidate_id": candidate_id,
            "experience_text": experience_text,
        }
    )

    for index, employment in enumerate(result.employments):
        employment.block_id = (
            f"{candidate_id}_employment_{index}"
        )
        employment.candidate_id = candidate_id

    return result.employments


