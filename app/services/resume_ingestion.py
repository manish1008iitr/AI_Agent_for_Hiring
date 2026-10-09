from uuid import uuid4

from app.services.resume_parser import parse_resume_text
from app.services.resume_chunker import chunk_resume
from app.services.vector_store import (
    get_vector_store,
    add_resume_chunks,
)


def ingest_resume(file_name: str, raw_text: str, candidate_id: str | None = None,) -> dict:
    """
    Parse, chunk, and store a resume in the vector database.

    Reusing a candidate_id replaces that candidate's existing chunks.
    """

    if not raw_text or not raw_text.strip():
        raise ValueError("Resume text cannot be empty.")

    if candidate_id is None:
        candidate_id = str(uuid4())

    # 1. Parse the raw text into logical sections.
    resume = parse_resume_text(
        candidate_id=candidate_id,
        file_name=file_name,
        raw_text=raw_text,
    )

    if not resume.sections:
        raise ValueError(
            "No resume sections were detected. "
            "Check the extracted text and section headings."
        )

    # 2. Convert sections into semantic chunks.
    documents = chunk_resume(resume)

    if not documents:
        raise ValueError("No chunks were generated from the resume.")

    # 3. Replace existing chunks for this candidate.
    vector_store = get_vector_store()
    vector_store.delete(where={"candidate_id": candidate_id})


    # 4. Store the newly generated chunks.
    chunk_ids = add_resume_chunks(documents)

    return {
        "candidate_id": candidate_id,
        "file_name": file_name,
        "section_count": len(resume.sections),
        "chunk_count": len(chunk_ids),
        "chunk_ids": chunk_ids,
        "status": "success",
    }

