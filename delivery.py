import os
from email.message import EmailMessage


OUTPUT_DIR = "generated_emails"


def save_email_locally(email_message: EmailMessage, filename: str) -> str:
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    file_path = os.path.join(OUTPUT_DIR, filename)

    with open(file_path, "wb") as f:
        f.write(email_message.as_bytes())

    return file_path
