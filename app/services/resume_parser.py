from app.services.resume_schema import (
    ProcessedResume,
    ResumeSection,
)
import re

KNOWN_SECTIONS = {
    "summary": "Summary",
    "professional summary": "Summary",
    "objective": "Objective",
    "career objective": "Objective",
    "experience": "Experience",
    "work experience": "Experience",
    "professional experience": "Experience",
    "education": "Education",
    "skills": "Skills",
    "technical skills": "Skills",
    "projects": "Projects",
    "personal projects": "Projects",
    "certifications": "Certifications",
    "achievements": "Achievements",
}




def normalize_heading(line: str) -> str:
    """Normalize a possible resume heading for comparison."""
    line = line.strip().lower()
    line = re.sub(r"[:\-–—]+$", "", line)
    line = re.sub(r"\s+", " ", line)
    return line.strip()


def parse_resume_text(candidate_id: str,file_name: str,raw_text: str) -> ProcessedResume:
    """
    Convert extracted resume text into a structured resume.

    This is the initial parser. File-format extraction
    will be added separately later.
    """

    sections = []
    current_section = None
    current_content = []

    for line in raw_text.splitlines():
        line = line.strip()

        if not line:
            continue

        normalized_line = normalize_heading(line)
        heading = KNOWN_SECTIONS.get(normalized_line)
        
        if heading:
            # Save the previous section before starting the next one.
            if current_section and current_content:
                sections.append(
                    ResumeSection(
                        section_name=current_section,
                        content="\n".join(current_content),
                    )
                )

            current_section = heading
            current_content = []

        elif current_section:
            current_content.append(line)

    # Save the final section.
    if current_section and current_content:
        sections.append(
            ResumeSection(
                section_name=current_section,
                content="\n".join(current_content),
            )
        )

    return ProcessedResume(
        candidate_id=candidate_id,
        file_name=file_name,
        raw_text=raw_text,
        sections=sections,
    )