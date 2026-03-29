import re
from email import policy
from email.parser import BytesParser
from html.parser import HTMLParser

# Define patterns for indicators
SUBJECT_URGENCY = re.compile(r'\b(URGENT|Immediate Action|Important Notice)\b', re.IGNORECASE)
GENERIC_GREETING = re.compile(r'Dear User', re.IGNORECASE)
ACTION_REQUEST = re.compile(r'(click|verify|update|reset)', re.IGNORECASE)
SUSPICIOUS_LINK_KEYWORDS = re.compile(r'(verify|update|reset|login)', re.IGNORECASE)


class LinkExtractor(HTMLParser):
    """Extracts all href links from HTML content."""
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'a':
            href = dict(attrs).get('href')
            if href:
                self.links.append(href)


def analyze_email(file_path: str) -> dict:
    # Parse .eml file
    with open(file_path, 'rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)

    indicators = []

    # Check subject for urgency
    subject = msg['Subject'] or ''
    if SUBJECT_URGENCY.search(subject):
        indicators.append("Urgency detected in subject")

    # Extract body: prefer HTML, fallback to plain
    body = ""
    body_part = msg.get_body(preferencelist=('html', 'plain'))
    if body_part is not None:
        body = body_part.get_content()

    # Generic greeting
    if GENERIC_GREETING.search(body):
        indicators.append("Generic greeting detected")

    # Suspicious action language
    if ACTION_REQUEST.search(body):
        indicators.append("Suspicious action language detected")

    # Header anomaly: From vs Reply-To
    from_addr = msg['From'] or ''
    reply_to = msg['Reply-To'] or ''
    if reply_to and reply_to not in from_addr:
        indicators.append("Header mismatch: From vs Reply-To")

    # HTML link analysis
    link_extractor = LinkExtractor()
    link_extractor.feed(body)
    for link in link_extractor.links:
        if SUSPICIOUS_LINK_KEYWORDS.search(link):
            indicators.append(f"Suspicious link detected: {link}")

    # Compute risk score: heuristic
    score = min(100, len(indicators) * 20)  # 20 points per indicator, max 100

    return {
        "file": file_path,
        "indicators": indicators,
        "risk_score": score,
        "explanation": " | ".join(indicators) if indicators else "No obvious phishing indicators detected"
    }
