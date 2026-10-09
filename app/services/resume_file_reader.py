## RESUME FILE SHOULD ONLY BE IN PDF FORMAT

from pathlib import Path
from pypdf import PdfReader
from app.services.resume_ingestion import ingest_resume


def extract_pdf_text(file_path: Path) -> str:
    """Extract text from a text-based PDF."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Resume file not found: {path}")

    if not path.is_file():
        raise ValueError(f"Expected a file, received: {path}")

    extension = path.suffix.lower()

    if extension != ".pdf":
        raise ValueError(
            f"Unsupported file format: {extension}. "
            "Supported formats are PDF only."
        )

    reader = PdfReader(str(file_path))

    pages = []

    for page in reader.pages:
        text = page.extract_text() or ""
        if text.strip():
            pages.append(text)

    return "\n\n".join(pages)


def process_resume(file_path:str, candidate_id: str | None = None):
    path = Path(file_path)

    raw_text = extract_pdf_text(path)

    result = ingest_resume(
        candidate_id=candidate_id,
        file_name=path.name,
        raw_text=raw_text,
    )

    return result




