from scenarios import PhishingScenario


def generate_subject(scenario: PhishingScenario) -> str:
    if scenario.urgency_level == "High":
        return "URGENT: Immediate Action Required"
    elif scenario.urgency_level == "Medium":
        return "Important Notice Regarding Your Account"
    else:
        return "Account Notification"


def generate_body(scenario: PhishingScenario) -> str:
    greeting = "Dear User,\n\n"

    body = (
        f"We are contacting you regarding the following issue:\n"
        f"{scenario.description}\n\n"
    )

    action = (
        f"Action Required:\n"
        f"{scenario.requested_action}.\n\n"
    )

    pressure = (
        "Failure to complete this action within the specified time "
        "may result in temporary limitations on your account.\n\n"
    )

    closing = (
        "If you believe this message was sent in error, please ignore it.\n\n"
        "Regards,\n"
        "System Support Team\n"
        "support@example.test"
    )

    return greeting + body + action + pressure + closing


def generate_email_content(scenario: PhishingScenario) -> dict:
    return {
        "subject": generate_subject(scenario),
        "body": generate_body(scenario)
    }
