import json

from langchain_core.tools import tool

from app.db.database import SessionLocal, engine, Base
from app.db.models import Job
from app.services.schemas import JobDescription

@tool
def save_job(job: JobDescription) -> int:
    """
    Save a generated job description to the database.

    Returns:
        The ID of the newly created job.
    """

    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()


    try:
        db_job = Job(
            title=job.title,
            summary=job.summary,
            responsibilities=json.dumps(job.responsibilities),
            must_have_skills=json.dumps(job.must_have_skills),
            nice_to_have_skills=json.dumps(job.nice_to_have_skills),
            minimum_experience_years=job.minimum_experience_years,
            education=json.dumps(job.education),
            location=job.location,
            employment_type=job.employment_type,
        )

        db.add(db_job)
        db.commit()
        db.refresh(db_job)
        return db_job.id
    
    finally:
        db.close()
