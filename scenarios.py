from dataclasses import dataclass
from typing import List


@dataclass
class PhishingScenario:
    id: int
    name: str
    description: str
    social_engineering_type: str
    urgency_level: str
    requested_action: str
    expected_red_flags: List[str]


SCENARIOS = [
    PhishingScenario(
        id=1,
        name="Fake Password Reset",
        description="A fictional IT department requests an urgent password reset.",
        social_engineering_type="Urgency",
        urgency_level="High",
        requested_action="Click password reset link",
        expected_red_flags=[
            "Urgent language",
            "Generic greeting",
            "Suspicious sender domain",
            "Action-required wording"
        ]
    ),
    PhishingScenario(
        id=2,
        name="Library Account Expiry",
        description="A fake university library warns about account expiration.",
        social_engineering_type="Authority",
        urgency_level="Medium",
        requested_action="Verify library account",
        expected_red_flags=[
            "Authority tone",
            "Unexpected request",
            "Domain mismatch",
            "Time pressure"
        ]
    )
]
