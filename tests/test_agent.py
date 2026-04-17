"""
Unit tests for Student Support AI Agent
"""

from src.agent import StudentSupportAgent


agent = StudentSupportAgent()


def test_attendance_query():
    response = agent.handle_query("A", "What is my attendance?")
    assert "80.0%" in response


def test_classes_attended_query():
    response = agent.handle_query("A", "How many classes did I attend?")
    assert "8 classes" in response


def test_payment_escalation():
    response = agent.handle_query("B", "Payment failed")
    assert response == "Escalating to human agent..."


def test_reschedule_escalation():
    response = agent.handle_query("A", "I want to reschedule my class")
    assert response == "Escalating to human agent..."


def test_angry_user_escalation():
    response = agent.handle_query("A", "Worst service ever")
    assert response == "Escalating to human agent..."


def test_booking_faq():
    response = agent.handle_query("A", "How to book class?")
    assert "portal" in response.lower()


def test_unknown_query():
    response = agent.handle_query("A", "Tell me a joke")
    assert response == "Escalating to human agent..."


def test_invalid_student():
    response = agent.handle_query("Z", "What is my attendance?")
    assert response == "Invalid student ID."