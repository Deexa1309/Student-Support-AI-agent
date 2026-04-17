"""
Utility helpers for the Student Support AI Agent.

This module contains reusable helper functions for:
- normalizing user input
- calculating attendance
- matching keywords
- validating student records
"""

from __future__ import annotations

import re
from typing import Iterable, Mapping, Any


def normalize_text(text: str) -> str:
    """
    Normalize user input for safer intent detection.

    Steps:
    - lowercase the text
    - strip leading/trailing spaces
    - collapse repeated whitespace
    - remove extra punctuation except apostrophes

    Args:
        text: Raw user input.

    Returns:
        Cleaned string.
    """
    cleaned = text.lower().strip()
    cleaned = re.sub(r"[^\w\s']", " ", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned


def calculate_attendance_percentage(attended: int, total: int) -> float:
    """
    Calculate attendance percentage safely.

    Args:
        attended: Number of attended classes.
        total: Total number of classes.

    Returns:
        Attendance percentage rounded to 2 decimal places.

    Raises:
        ValueError: If attended or total is invalid.
    """
    if total <= 0:
        raise ValueError("Total classes must be greater than 0.")
    if attended < 0:
        raise ValueError("Attended classes cannot be negative.")
    if attended > total:
        raise ValueError("Attended classes cannot exceed total classes.")

    percentage = (attended / total) * 100
    return round(percentage, 2)


def contains_any_keyword(text: str, keywords: Iterable[str]) -> bool:
    """
    Check whether the given text contains any keyword/phrase.

    Args:
        text: Normalized text.
        keywords: A list/set/tuple of words or phrases.

    Returns:
        True if at least one keyword is found, else False.
    """
    return any(keyword in text for keyword in keywords)


def get_student_record(
    student_id: str,
    students: Mapping[str, Mapping[str, Any]],
) -> Mapping[str, Any]:
    """
    Fetch a student record by ID.

    Args:
        student_id: Student identifier such as 'A' or 'B'.
        students: Student data mapping.

    Returns:
        The student's record.

    Raises:
        KeyError: If the student ID is not found.
    """
    normalized_id = student_id.strip().upper()

    if normalized_id not in students:
        raise KeyError(f"Student ID '{student_id}' not found.")

    return students[normalized_id]