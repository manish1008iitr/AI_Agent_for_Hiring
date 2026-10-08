from sqlalchemy import Column, Integer, String, Text

from app.db.database import Base

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



