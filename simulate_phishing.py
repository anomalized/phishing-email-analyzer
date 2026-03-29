import os
from scenarios import SCENARIOS
from email_generator import generate_email_content
from header_generator import generate_headers
from delivery import save_email_locally
from analyzer import analyze_email

def run_simulation():
    print("Available Scenarios:")
    for scenario in SCENARIOS:
        print(f"{scenario.id}: {scenario.name} ({scenario.urgency_level} urgency)")

    # User selects scenario
    selected_id = int(input("Enter Scenario ID to simulate: "))
    scenario = next((s for s in SCENARIOS if s.id == selected_id), None)
    if scenario is None:
        print("Invalid Scenario ID.")
        return

    # Generate email content
    email_content = generate_email_content(scenario)

    # Generate headers
    email_msg = generate_headers(email_content)

    # Save email safely
    filename = f"simulation_{scenario.id}.eml"
    file_path = save_email_locally(email_msg, filename)
    print(f"Email saved locally: {file_path}")

    # Analyze email
    analysis = analyze_email(file_path)
    print("\n--- Analysis Report ---")
    print(f"Scenario: {scenario.name}")
    print(f"Risk Score: {analysis['risk_score']}")
    print("Indicators Detected:")
    for ind in analysis['indicators']:
        print("-", ind)
    print("Explanation:", analysis['explanation'])
    print("----------------------")

if __name__ == "__main__":
    run_simulation()
