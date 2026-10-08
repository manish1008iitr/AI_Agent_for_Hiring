from langchain_core.prompts import ChatPromptTemplate
from app.services.llm import get_llm

#Function call to get llm 
llm = get_llm()

def generate_job_description(hr_prompt: str) -> str:
    """
    Generate a job description from an HR's natural-language request.
    """

    prompt = ChatPromptTemplate.from_messages(
        [("system", """
            You are an expert technical recruiter.

            Your task is to convert an HR's rough hiring request
            into a clear and professional job description.

            The job description should contain:

            1. Job Title
            2. Job Summary
            3. Responsibilities
            4. Required Skills
            5. Preferred Skills
            6. Experience Requirements
            7. Education Requirements
            8. Location / Work Mode

            Important:
            - Do not invent requirements that are not reasonably implied.
            - Clearly distinguish required skills from preferred skills.
            - Keep the description concise and professional.
            """
            ),
            ("human","""Here is the HR's hiring request:{hr_prompt}""")
        ]
    )

    chain = prompt | llm

    response = chain.invoke(
        {"hr_prompt": hr_prompt}
    )

    return response.content