import os
import csv
import matplotlib.pyplot as plt
from analyzer import analyze_email
from scenarios import SCENARIOS

EMAIL_DIR = "generated_emails"
REPORT_CSV = "phishing_report.csv"
OUTPUT_IMAGE = "phishing_risk_chart.png"

# Color Palette
COLOR_MAROON = "#800000"
COLOR_ZINC_BLUE = "#5D6D7E"

# Map scenario filenames to scenario names
scenario_map = {f"simulation_{s.id}.eml": s.name for s in SCENARIOS}

def generate_report():
    results = []

    # Analyze all .eml files
    if not os.path.exists(EMAIL_DIR):
        print(f"Directory {EMAIL_DIR} not found.")
        return

    for filename in os.listdir(EMAIL_DIR):
        if filename.endswith(".eml"):
            file_path = os.path.join(EMAIL_DIR, filename)
            analysis = analyze_email(file_path)
            scenario_name = scenario_map.get(filename, filename)
            results.append({
                "Scenario": scenario_name,
                "File": filename,
                "Risk Score": analysis['risk_score'],
                "Indicators": "; ".join(analysis['indicators'])
            })

    if not results:
        print("No data to plot.")
        return

    # Save CSV
    with open(REPORT_CSV, "w", newline="") as csvfile:
        fieldnames = ["Scenario", "File", "Risk Score", "Indicators"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)

    print(f"Report saved as {REPORT_CSV}")

    # Sort results by Risk Score for a cleaner visual flow
    results.sort(key=lambda x: x["Risk Score"], reverse=True)
    
    scenarios = [r["Scenario"] for r in results]
    scores = [r["Risk Score"] for r in results]

    # Visual Enhancements
    # We use subplots to handle the layout better without explicit .figure() calls
    fig, ax = plt.subplots(figsize=(12, 7))

    # Create the bar chart
    bars = ax.bar(scenarios, scores, color=COLOR_MAROON, edgecolor=COLOR_ZINC_BLUE, linewidth=1, width=0.7)

    # Styling the axes and labels
    ax.set_ylabel("Risk Score", fontsize=12, fontweight='bold', color=COLOR_ZINC_BLUE)
    ax.set_title("Phishing Scenario Risk Analysis", fontsize=16, fontweight='bold', color=COLOR_MAROON, pad=20)
    
    # Customize the ticks
    plt.xticks(rotation=30, ha='right', fontsize=10, color=COLOR_ZINC_BLUE)
    plt.yticks(fontsize=10, color=COLOR_ZINC_BLUE)

    # Add a subtle horizontal grid using the Zinc Blue color
    ax.yaxis.grid(True, linestyle='--', alpha=0.4, color=COLOR_ZINC_BLUE)
    ax.set_axisbelow(True) # Put grid behind bars

    # Remove the top and right spines for a modern look
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(COLOR_ZINC_BLUE)
    ax.spines['bottom'].set_color(COLOR_ZINC_BLUE)

    # Add value labels on top of bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{height}', ha='center', va='bottom', 
                fontsize=10, fontweight='bold', color=COLOR_MAROON)

    plt.tight_layout()
    plt.savefig(OUTPUT_IMAGE, dpi=300)
    print(f"Visual report saved as {OUTPUT_IMAGE}")

if __name__ == "__main__":
    generate_report()