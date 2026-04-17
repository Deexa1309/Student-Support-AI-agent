"""
Data layer for the Student Support AI Agent.

This module stores:
- student records
- FAQ responses
- escalation keywords

"""

from typing import Dict, Set


# Student Records (Sample Database)


students: Dict[str, Dict[str, object]] = {
    "A": {
        "name": "Aarav Sharma",
        "attended": 8,
        "total": 10,
        "payments": "done",
    },
    "B": {
        "name": "Bhavna Kapoor",
        "attended": 3,
        "total": 10,
        "payments": "failed",
    },
    "C": {
        "name": "Chetan Verma",
        "attended": 9,
        "total": 12,
        "payments": "done",
    },
    "D": {
        "name": "Divya Mehta",
        "attended": 5,
        "total": 8,
        "payments": "pending",
    },
    "E": {
        "name": "Eshan Gupta",
        "attended": 7,
        "total": 9,
        "payments": "done",
    },
    "F": {
        "name": "Farah Khan",
        "attended": 2,
        "total": 10,
        "payments": "failed",
    },
}


# FAQ Responses


faq_responses: Dict[str, str] = {
    "how to book class": (
        "You can book a class from the student portal under "
        "'Bookings' > 'Available Slots'."
    ),
    "how do i book class": (
        "You can book a class from the student portal under "
        "'Bookings' > 'Available Slots'."
    ),
    "book class": (
        "Open the student portal and go to the Bookings section."
    ),
    "how to cancel class": (
        "You can cancel a booked class from the portal under "
        "'My Bookings'."
    ),
    "how to join class": (
        "Open your dashboard and click the active session link."
    ),
    "where is my schedule": (
        "Your weekly class schedule is available on the dashboard."
    ),
    "how to reset password": (
        "Use the 'Forgot Password' option on the login page."
    ),
    "how to contact support": (
        "You can contact support via email or live chat in the portal."
    ),
    "when is next class": (
        "Please check your dashboard calendar for upcoming classes."
    ),
    "how to download receipt": (
        "Go to Payments > Transaction History to download receipts."
    ),
}


# Escalation Triggers


escalation_keywords: Set[str] = {
    # Payments
    "payment",
    "failed",
    "failure",
    "refund",
    "charged twice",
    "double charged",
    "billing",
    "invoice issue",

    # User frustration / angry sentiment
    "angry",
    "frustrated",
    "upset",
    "complaint",
    "worst",
    "terrible",
    "bad service",
    "not happy",
    "disappointed",

    # Scheduling issues
    "reschedule",
    "rescheduling",
    "change class",
    "change my class",
    "move class",
    "cancel and rebook",

    # Urgent help
    "urgent",
    "immediately",
    "asap",
    "help now",

    # Technical issues
    "cannot login",
    "login failed",
    "portal not working",
    "system error",
}


# Valid Student IDs


valid_student_ids: Set[str] = set(students.keys())