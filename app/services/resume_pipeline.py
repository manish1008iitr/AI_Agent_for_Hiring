
from pathlib import Path
from uuid import uuid4

from app.services.resume_file_reader import extract_pdf_text
from app.services.resume_ingestion import ingest_resume
from app.services.candidate_utils import generate_candidate_id

from app.db.database import Base, engine, SessionLocal
from app.db.models import Candidate, Resume



def process_resume_file(file_path:str, email:str, name:str):
    path = Path(file_path)

    raw_text = extract_pdf_text(path)
    candidate_id = generate_candidate_id(email)
    print(candidate_id)

    # Ensure the database tables exist.
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()
    resume_record_id = None

    try:
        # Find the candidate or create a new candidate record.
        candidate = (
            db.query(Candidate)
            .filter(Candidate.candidate_id == candidate_id)
            .first()
        )

        if candidate is None:
            candidate = Candidate(
                candidate_id=candidate_id,
                email=email.strip().lower(),
                full_name = name
            )
            db.add(candidate)
            db.flush()

        # Create a resume record before processing begins.
        resume_record = Resume(
            candidate_id=candidate_id,
            file_name=path.name,
            file_path=str(path.resolve()),
            status="processing",
        )
        db.add(resume_record)
        db.commit()
        db.refresh(resume_record)

        resume_record_id = resume_record.id

        try:
            # Extract text from the PDF or DOCX.
            raw_text = extract_pdf_text(path)

            # Chunk the resume and index it in Chroma.
            result = ingest_resume(
                candidate_id=candidate_id,
                file_name=path.name,
                raw_text=raw_text,
            )

            # Update the database after successful processing.
            resume_record.status = "processed"
            resume_record.section_count = result["section_count"]
            resume_record.chunk_count = result["chunk_count"]

            db.commit()

            result["resume_record_id"] = resume_record_id
            result["status"] = "processed"

            return result
        
        except Exception:
                # Preserve a failure status if processing fails.
                db.rollback()

    finally:
            db.close()

