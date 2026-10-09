from app.db.database import Base

from datetime import datetime

from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    summary = Column(Text, nullable=False)

    responsibilities = Column(Text, nullable=False)

    must_have_skills = Column(Text, nullable=False)

    nice_to_have_skills = Column(Text, nullable=False)

    minimum_experience_years = Column(Integer, nullable=False)

    education = Column(Text, nullable=True)

    location = Column(Text, nullable=True)

    location = Column(String, nullable=True)

    employment_type = Column(String, nullable=True)

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    candidate_id = Column(String, unique=True, nullable=False, index=True)

    full_name = Column(String, nullable=True)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    resumes = relationship(
        "Resume",
        back_populates="candidate",
        cascade="all, delete-orphan",
    )


class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    candidate_id = Column(
        String,
        ForeignKey("candidates.candidate_id"),
        nullable=False,
        index=True,
    )

    file_name = Column(String, nullable=False)
    file_path = Column(String, nullable=False)

    status = Column(String, default="uploaded", nullable=False)
    section_count = Column(Integer, default=0, nullable=False)
    chunk_count = Column(Integer, default=0, nullable=False)

    uploaded_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    candidate = relationship("Candidate", back_populates="resumes")





