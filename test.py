"""
Demonstration script for phishing email analysis.

This script demonstrates how to:
1. Generate phishing emails
2. Save them as .eml files
3. Analyze them for phishing indicators
"""

from email.message import EmailMessage
from analyzer import analyze_email


def demo_html_email_analysis():
    """Demonstrate analyzing an HTML-format phishing email."""
    # Create a dummy HTML email locally
    msg = EmailMessage()
    msg['From'] = 'System Support <support@alerts-example.test>'
    msg['To'] = 'user@university.test'
    msg['Subject'] = 'URGENT: Verify Your Account'
    msg['Reply-To'] = 'support@response-example.test'
    msg.set_content("""<html>
<body>
<p>Dear User,</p>
<p>Please <a href="http://example-bank.test/reset">reset your password</a> immediately.</p>
</body>
</html>""", subtype='html')

    # Save as .eml
    with open("generated_emails/html_test.eml", "wb") as f:
        f.write(msg.as_bytes())

    # Analyze
    result = analyze_email("generated_emails/html_test.eml")
    print("Analysis Result:")
    print(result)


if __name__ == "__main__":
    demo_html_email_analysis()




