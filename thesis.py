from collections import defaultdict
import fitz  # PyMuPDF
import re
import csv

# Step 1: Define relevant keywords
KEYWORDS = [
    "federated learning", "fl", "differential privacy", "dp", 
    "homomorphic encryption", "he", "secure multiparty computation", "smpc",
    "trusted execution environment", "tee", "shamir secret sharing",
    "blockchain", "quantum", "ring signature", "zero knowledge proof",
    "ehr", "phi", "hipaa", "gdpr", "medical", "clinical", "patient",
    "diagnos", "treatment", "icu", "x-ray", "ct", "mri", "wearable",
    "accuracy", "auc", "f1", "overhead", "latency", "scalability",
    "communication cost", "privacy budget", "epsilon", "computational",
    "inference attack", "membership attack", "model inversion",
    "data poisoning", "gradient leakage", "byzantine", "adversarial",
    "backdoor", "poisoning"
]

def keyword_score(text):
    """Count keyword hits in a chunk of text."""
    try:
        text = text.lower()
        return sum(text.count(keyword) for keyword in KEYWORDS)
    except Exception as e:
        print(f"Error in keyword_score: {e}")
        return 0

# Step 2: Extract entries
def extract_entries(pdf_path):
    """Extract entries from the PDF."""
    try:
        doc = fitz.open(pdf_path)
        text = "\n".join(page.get_text() for page in doc)
        print(f"Total extracted text length: {len(text)} characters")
        entries = re.split(r"\n(?=Author:)", text)
        entries = [entry.strip() for entry in entries if len(entry.strip()) > 300]
        print(f"Extracted {len(entries)} entries from PDF.")
        return entries
    except Exception as e:
        print(f"Error in extract_entries: {e}")
        return []

# Step 3: Metadata extractor
def extract_metadata(entry):
    """Extract metadata from an entry."""
    metadata = {}
    # Authors
    author_match = re.search(r'Author:\s*(.+?)\s*(?=Subject:|Is Part Of:|Description:|$)', entry, re.DOTALL)
    metadata["authors"] = author_match.group(1).strip() if author_match else "Unknown"
    # DOI
    doi_match = re.search(r'(10\.\d{4,9}/[^\s";]+)', entry)
    metadata["doi"] = doi_match.group(1) if doi_match else "Unknown"
    # Publisher
    publisher_match = re.search(r'Publisher:\s*(.+)', entry)
    metadata["publisher"] = publisher_match.group(1).strip() if publisher_match else "Unknown"
    # Year
    year_match = re.search(r'(\b20[1-2][0-9]\b)', entry)
    metadata["year"] = year_match.group(1) if year_match else "Unknown"
    # Description
    desc_match = re.search(r'(Description|Abstract):\s*(.+?)(?=\n[A-Z][a-z]+:|$)', entry, re.DOTALL)
    metadata["description"] = desc_match.group(2).strip() if desc_match else "No description found"
    return metadata

# Step 4: Scoring
def rank_entries(entries, top_n=10):
    """Rank entries by keyword score."""
    try:
        scored = [(entry, keyword_score(entry)) for entry in entries]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_n]
    except Exception as e:
        print(f"Error in rank_entries: {e}")
        return []

# Step 5: Save top results to both CSV and TXT
def save_top_results_to_files(ranked_entries):
    """Save top study results to both CSV and TXT formats."""
    try:
        with open("results.csv", "w", newline="", encoding="utf-8") as f_csv, \
             open("results.txt", "w", encoding="utf-8") as f_txt:
            writer = csv.writer(f_csv)
            writer.writerow(["Rank", "Score", "Authors", "DOI", "Publisher", "Description"])
            for i, (entry, score) in enumerate(ranked_entries, 1):
                meta = extract_metadata(entry)
                authors = meta["authors"]
                doi = meta["doi"]
                publisher = meta["publisher"]
                description = meta["description"][:300]
                # Write to CSV
                writer.writerow([i, score, authors, doi, publisher, description])
                # Write to TXT
                f_txt.write(f"--- Top {i} Study (Score: {score}) ---\n")
                f_txt.write(f"Authors   : {authors}\n")
                f_txt.write(f"DOI       : {doi}\n")
                f_txt.write(f"Publisher : {publisher}\n")
                f_txt.write(f"Description: {description}\n\n")
        print("✅ Results saved to results.csv and results.txt")
    except Exception as e:
        print(f"❌ Error saving results: {e}")

# Step 6: Main analysis and printing
def analyze_pdf_for_top_studies(pdf_path, top_n=10):
    """Main function to select and save top 10 studies."""
    try:
        entries = extract_entries(pdf_path)
        ranked = rank_entries(entries, top_n)
        for i, (entry, score) in enumerate(ranked, 1):
            meta = extract_metadata(entry)
            print(f"--- Top {i} Study (Score: {score}) ---")
            print(f"Authors   : {meta['authors']}")
            print(f"DOI       : {meta['doi']}")
            print(f"Publisher : {meta['publisher']}")
            print(f"Description: {meta['description'][:300]}")
        save_top_results_to_files(ranked)
        print("\nSelection complete. Results saved to:")
        print("- results.csv (top 10 metadata)")
        print("- results.txt (top 10 metadata)")
    except Exception as e:
        print(f"❌ Error in analyze_pdf_for_top_studies: {e}")

# Run it
if __name__ == "__main__":
    pdf_path = "Ex Libris Discovery - privacy-Preserving Techniques in Federated Learning for Secure Healthcare Data Sharing.pdf"
    print(f"Opening PDF: {pdf_path}")
    analyze_pdf_for_top_studies(pdf_path)
