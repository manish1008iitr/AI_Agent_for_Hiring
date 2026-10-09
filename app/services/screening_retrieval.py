
from app.services.vector_store import search_resumes


def build_screening_query(job: dict) -> str:
    """Build a semantic search query from a saved job description."""

    must_have = ", ".join(job.get("must_have_skills", []))
    nice_to_have = ", ".join(job.get("nice_to_have_skills", []))
    responsibilities = "\n".join(job.get("responsibilities", []))

    return f"""
    Job title: {job.get("title", "")}
    Job summary: {job.get("summary", "")}

    Mandatory skills: {must_have}
    Preferred skills: {nice_to_have}

    Responsibilities:{responsibilities}

    Find resume evidence of relevant skills, work experience,
    projects, and responsibilities for this role.
    """


def retrieve_resume_evidence(job: dict, k: int = 10) -> list[dict]:
    """Retrieve resume chunks relevant to a job."""

    query = build_screening_query(job)
    documents = search_resumes(query=query, k=k)

    results = []

    for document in documents:
        results.append({
            "candidate_id": document.metadata.get("candidate_id"),
            "file_name": document.metadata.get("file_name"),
            "section": document.metadata.get("section"),
            "content": document.page_content,
        })

    return results


