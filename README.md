# Phishing Email Analyzer & Simulator

A comprehensive Python toolkit for analyzing emails for phishing indicators and simulating realistic phishing scenarios for security awareness and testing.

## Features

- **Email Analysis**: Detects phishing red flags in EML files
- **Risk Scoring**: Computes risk level based on multiple indicators
- **Phishing Simulation**: Generate realistic phishing emails for testing
- **Header Analysis**: Extracts and analyzes email headers
- **Link Extraction**: Identifies suspicious links in email content
- **Custom Scenarios**: Predefined phishing scenarios for realistic simulations
- **Report Generation**: CSV and visual reporting of results

## Prerequisites

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

```bash
git clone https://github.com/yourusername/phishing-email-analyzer.git
cd phishing-email-analyzer
```

Optional: Create a virtual environment (recommended)
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

## Project Structure

```
phishing-email-analyzer/
├── analyzer.py              # Core email analysis engine
├── simulate_phishing.py      # Phishing simulation runner
├── email_generator.py        # Generate phishing email content
├── header_generator.py       # Create email headers
├── scenarios.py              # Predefined phishing scenarios
├── delivery.py               # Save and manage emails
├── reporting.py              # Generate analysis reports
├── test.py                   # Demonstration scripts
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
├── README.md                 # This file
└── generated_emails/         # Output: Simulated emails (not tracked)
```

## Usage

### Analyze an Email

```python
from analyzer import analyze_email

analysis = analyze_email("path/to/email.eml")
print(f"Risk Score: {analysis['risk_score']}")
print(f"Indicators: {analysis['indicators']}")
```

### Run Phishing Simulation

```bash
python simulate_phishing.py
```

This will:
1. Display available phishing scenarios
2. Prompt you to select a scenario
3. Generate a phishing email
4. Analyze it and output results

### Generate Report

```python
from reporting import generate_report

generate_report("phishing_report.csv")
```

## Detection Indicators

The analyzer checks for:

- **Subject Line Issues**
  - Urgency markers (URGENT, Immediate Action, Important Notice)
  
- **Greeting Issues**
  - Generic greetings ("Dear User" instead of specific name)
  
- **Call-to-Action**
  - Action request keywords (click, verify, update, reset)
  
- **Suspicious Links**
  - Mismatched display text vs. actual URL
  - Verification/update/reset keywords in URLs
  
- **Email Header Anomalies**
  - Spoofed sender addresses
  - Missing DKIM/SPF signatures

## Phishing Scenarios

Scenarios define realistic phishing attempts with parameters:
- Urgency level (Low, Medium, High, Critical)
- Target domain
- Action type
- Email template

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is designed for educational purposes and authorized security testing only. Unauthorized access or use of this tool for malicious purposes is illegal.

Example scenarios:
- Account suspension threats
- Payment verification requests
- Security alert responses
- Credential verification

## Output Files

- **phishing_report.csv**: Structured analysis results (email, risk score, indicators)
- **phishing_risk_chart.png**: Visual representation of phishing risks
- **generated_emails/**: EML files of simulated phishing attempts
- Console output: Real-time analysis feedback

## Risk Scoring

Risk scores range from **0-100**:
- **0-25**: Low risk (legitimate email likely)
- **26-50**: Medium risk (suspicious elements)
- **51-75**: High risk (multiple indicators)
- **76-100**: Critical risk (likely phishing)

## Example Output

```
--- Analysis Report ---
Scenario: Account Suspension Warning
Risk Score: 92
Indicators Detected:
- Urgent subject line detected
- Generic greeting without personalization
- Suspicious link found
- Action request present
Explanation: High confidence this is a phishing attempt. Multiple red flags detected including urgent language, generic greeting, and request for immediate action.
```

## Error Handling

- Missing EML files: Returns error message
- Malformed emails: Graceful parsing with error reporting
- Invalid scenarios: User-friendly error messages

## Testing

Run unit tests:

```bash
python test.py
```

## Security Notes

⚠️ **Important**: This tool is for authorized security testing only.

- Use only on emails you own or have permission to analyze
- Simulated emails should only be deployed in controlled environments
- All usage must comply with applicable laws and policies

## License

Internal Use - Cybersecurity Project
