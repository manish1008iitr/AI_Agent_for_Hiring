import hashlib


def generate_candidate_id(email: str) -> str:
    if not email or not email.strip():
        raise ValueError("Candidate email cannot be empty.")

    normalized_email = email.strip().lower()

    return hashlib.md5(
        normalized_email.encode("utf-8")
    ).hexdigest()