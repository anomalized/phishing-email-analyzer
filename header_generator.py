from email.message import EmailMessage
from datetime import datetime
import uuid


def generate_headers(email_content: dict) -> EmailMessage:
    msg = EmailMessage()

    msg["From"] = "System Support Team <support@alerts-example.test>"
    msg["To"] = "user@university.test"
    msg["Reply-To"] = "support@response-example.test"
    msg["Subject"] = email_content["subject"]
    msg["Date"] = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")
    msg["Message-ID"] = f"<{uuid.uuid4()}@alerts-example.test>"

    msg.set_content(email_content["body"])

    return msg
