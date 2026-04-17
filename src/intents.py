"""
Intent classification module for the Student Support AI Agent.

This module converts raw user queries into structured intents.
"""

from __future__ import annotations

from enum import Enum
from typing import Final

from src.utils import normalize_text


class Intent(str, Enum):
    ATTENDANCE_PERCENTAGE = "attendance_percentage"
    CLASSES_ATTENDED = "classes_attended"
    FAQ_BOOKING = "faq_booking"
    FAQ_GENERAL = "faq_general"
    ESCALATE_PAYMENT = "escalate_payment"
    ESCALATE_RESCHEDULE = "escalate_reschedule"
    ESCALATE_ANGRY = "escalate_angry"
    UNKNOWN = "unknown"


ATTENDANCE_KEYWORDS: Final = {
    "attendance",
    "attendance percentage",
    "my attendance",
}

CLASSES_ATTENDED_KEYWORDS: Final = {
    "how many classes did i attend",
    "classes did i attend",
    "classes attended",
    "attended how many",
}

BOOKING_KEYWORDS: Final = {
    "book class",
    "how to book class",
    "how do i book class",
}

PAYMENT_KEYWORDS: Final = {
    "payment failed",
    "payment",
    "refund",
    "charged twice",
    "billing issue",
}

RESCHEDULE_KEYWORDS: Final = {
    "reschedule",
    "reschedule class",
    "change my class",
    "move class",
}

ANGRY_KEYWORDS: Final = {
    "angry",
    "frustrated",
    "worst",
    "terrible",
    "bad service",
    "upset",
    "complaint",
}


def classify_intent(query: str) -> Intent:
    """
    Convert a user query into an intent.

    Priority matters:
    urgent/escalation intents checked first.
    """
    text = normalize_text(query)

    # Escalation first
    if any(keyword in text for keyword in PAYMENT_KEYWORDS):
        return Intent.ESCALATE_PAYMENT

    if any(keyword in text for keyword in RESCHEDULE_KEYWORDS):
        return Intent.ESCALATE_RESCHEDULE

    if any(keyword in text for keyword in ANGRY_KEYWORDS):
        return Intent.ESCALATE_ANGRY

    # Data queries
    if any(keyword in text for keyword in CLASSES_ATTENDED_KEYWORDS):
        return Intent.CLASSES_ATTENDED

    if any(keyword in text for keyword in ATTENDANCE_KEYWORDS):
        return Intent.ATTENDANCE_PERCENTAGE

    # FAQs
    if any(keyword in text for keyword in BOOKING_KEYWORDS):
        return Intent.FAQ_BOOKING

    return Intent.UNKNOWN