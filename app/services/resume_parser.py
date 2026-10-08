from app.services.resume_schema import (
    ProcessedResume,
    ResumeSection,
)

def parse_resume_text(candidate_id: str,file_name: str,raw_text: str) -> ProcessedResume:
    """
    Convert extracted resume text into a structured resume.

    This is the initial parser. File-format extraction
    will be added separately later.
    """

    sections = []
    current_section = None
    current_content = []

    known_sections = {
        "summary",
        "objective",
        "experience",
        "work experience",
        "education",
        "skills",
        "projects",
        "certifications",
        "achievements",
    }

    for line in raw_text.splitlines():

        line = line.strip()

        if not line:
            continue

        normalized_line = line.lower()

        if normalized_line in known_sections:
            if current_section and current_content:
                sections.append(
                    ResumeSection(
                        section_name=current_section,
                        content="\n".join(current_content),
                    )
                )

            current_section = line
            current_content = []

        else:
            if current_section:
                current_content.append(line)

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