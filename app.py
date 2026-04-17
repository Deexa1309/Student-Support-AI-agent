"""
Student Support AI Agent
CLI Entry Point
"""

from __future__ import annotations

from src.agent import StudentSupportAgent


WELCOME_BANNER = """
========================================
   Student Support AI Agent
========================================
Type 'exit' anytime to quit.
"""


def main() -> None:
    """
    Run command-line interface.
    """
    agent = StudentSupportAgent()

    print(WELCOME_BANNER)

    student_id = input("Enter Student ID: ").strip().upper()

    while True:
        try:
            query = input("\nAsk your question: ").strip()

            if query.lower() == "exit":
                print("Goodbye!")
                break

            if not query:
                print("Please enter a valid question.")
                continue

            response = agent.handle_query(student_id, query)

            print(f"\nAgent: {response}")

        except KeyboardInterrupt:
            print("\nSession closed.")
            break

        except Exception as error:
            print(f"\nUnexpected error: {error}")
            break


if __name__ == "__main__":
    main()