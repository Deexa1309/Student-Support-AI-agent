"""
Main AI Agent logic for Student Support AI Agent.
"""

from __future__ import annotations

from data.students import students, faq_responses
from src.intents import Intent, classify_intent
from src.utils import (
    calculate_attendance_percentage,
    get_student_record,
    normalize_text,
)


ESCALATION_MESSAGE = "Escalating to human agent..."


class StudentSupportAgent:
    """
    Main support agent class.
    """

    def __init__(self) -> None:
        self.students = students
        self.faq_responses = faq_responses

    def handle_query(self, student_id: str, query: str) -> str:
        """
        Main public method to process a user query.

        Args:
            student_id: Student identifier (A, B, C...)
            query: Raw user message

        Returns:
            Final response string
        """
        try:
            student = get_student_record(student_id, self.students)
        except KeyError:
            return "Invalid student ID."

        intent = classify_intent(query)
        cleaned_query = normalize_text(query)

        # ------------------------------
        # Escalation Intents
        # ------------------------------
        if intent in {
            Intent.ESCALATE_PAYMENT,
            Intent.ESCALATE_RESCHEDULE,
            Intent.ESCALATE_ANGRY,
            Intent.UNKNOWN,
        }:
            return ESCALATION_MESSAGE

        # ------------------------------
        # Attendance %
        # ------------------------------
        if intent == Intent.ATTENDANCE_PERCENTAGE:
            attended = student["attended"]
            total = student["total"]

            percentage = calculate_attendance_percentage(
                attended,
                total,
            )

            return (
                f"Your attendance is {percentage}% "
                f"({attended}/{total} classes attended)."
            )

        # ------------------------------
        # Count Classes Attended
        # ------------------------------
        if intent == Intent.CLASSES_ATTENDED:
            attended = student["attended"]

            return f"You attended {attended} classes."

        # ------------------------------
        # FAQ Booking
        # ------------------------------
        if intent == Intent.FAQ_BOOKING:
            for key, response in self.faq_responses.items():
                if key in cleaned_query:
                    return response

            return (
                "You can book a class from the student portal "
                "under the Bookings section."
            )

        # ------------------------------
        # Fallback Safety
        # ------------------------------
        return ESCALATION_MESSAGE