import fitz  # PyMuPDF
import re
from collections import Counter
import csv
import matplotlib.pyplot as plt

# This script analyzes a PDF document to extract and rank studies based on the presence of specific keywords related to privacy-preserving techniques in federated learning for secure healthcare data sharing.
# Step 1: Define relevant keywords
KEYWORDS = [
    "federated learning", "privacy", "homomorphic encryption", "differential privacy",
    "secure data", "healthcare", "medical", "GDPR", "HIPAA", "encryption", "SMPC",
    "TEE", "blockchain", "secure aggregation", "data anonymization"
]

def keyword_score(text):
    """Count keyword hits in a chunk of text."""
    try:
        text = text.lower()
        return sum(text.count(keyword) for keyword in KEYWORDS)
    except Exception as e:
        print(f"Error in keyword_score: {e}")
        return 0

# Step 2: Extract text blocks from PDF
def extract_entries(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        print(f"Total extracted text length: {len(text)} characters")
        if not text:
            print("No text extracted from PDF. It may be image-based.")
            return []
        # Heuristic: split entries based on visual spacing or line structure
        potential_entries = re.split(r'\n(?=[A-Z].{5,})', text)
        clean_entries = [entry.strip() for entry in potential_entries if len(entry.strip()) > 200]
        print(f"Extracted {len(clean_entries)} entries from PDF.")
        if not clean_entries:
            print("No entries met the length criteria. First 500 chars of text:")
            print(text[:500])
        return clean_entries
    except Exception as e:
        print(f"Error in extract_entries: {e}")
        return []

# Step 3: Score and rank entries
def rank_entries(entries, top_n=10):
    try:
        scored_entries = [(entry, keyword_score(entry)) for entry in entries]
        scored_entries = sorted(scored_entries, key=lambda x: x[1], reverse=True)
        return scored_entries[:top_n]
    except Exception as e:
        print(f"Error in rank_entries: {e}")
        return []

# Step 4: Plot scores
def plot_scores(ranked):
    try:
        scores = [score for _, score in ranked]
        ranks = range(1, len(ranked) + 1)
        plt.bar(ranks, scores, color='skyblue')
        plt.xlabel("Rank")
        plt.ylabel("Keyword Score")
        plt.title("Top Entries by Keyword Score")
        plt.savefig("scores_plot.png")
        plt.close()
        print("Plot saved to scores_plot.png")
    except Exception as e:
        print(f"Error in plot_scores: {e}")

# Step 5: Run analysis, save to CSV, and plot
def analyze_pdf_for_top_studies(pdf_path, top_n=10):
    try:
        entries = extract_entries(pdf_path)
        ranked = rank_entries(entries, top_n)
        plot_scores(ranked)  # Generate plot
        with open("results.csv", "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Rank", "Score", "Entry"])
            for i, (entry, score) in enumerate(ranked, 1):
                writer.writerow([i, score, entry[:1000]])
                print(f"--- Top {i} Study (Score: {score}) ---\n")
                print(entry[:1000], "...")
                print("\n" + "="*80 + "\n")
        print(f"Results saved to results.csv")
    except Exception as e:
        print(f"Error in analyze_pdf_for_top_studies: {e}")

# Example usage
if __name__ == "__main__":
    pdf_file_path = "Ex Libris Discovery - privacy-Preserving Techniques in Federated Learning for Secure Healthcare Data Sharing.pdf"
    try:
        print(f"Opening PDF: {pdf_file_path}")
        analyze_pdf_for_top_studies(pdf_file_path)
    except Exception as e:
        print(f"Error: {e}")