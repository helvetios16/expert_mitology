from typing import Any


def set_admission(value: bool) -> dict[str, bool]:
    """Return a dictionary containing the admission result."""
    return {"is_admitted": value}


def set_course(course_id: str) -> dict[str, str]:
    """Return the course id as a dictionary."""
    return {"course_id": course_id}


def send_email(mail_to: str, mail_content: str, meal: str) -> str | None:
    """Send an email."""
    result: str | None = None

    if meal is not None:
        # API call here
        result = "sent"

    return result
