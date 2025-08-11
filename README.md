# Privacy-Preserving Federated Learning for Healthcare

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository contains all materials for my MSc thesis:  
**"A Critical Analysis of Privacy-Preserving Techniques in Federated Learning for Secure Healthcare Data Sharing"**  
*University of East London, 2025*

## 📌 Key Features
- **Automated Analysis Pipeline**: Python scripts (`thesis.py`, `thesis_analysis.py`) for evaluating 20 peer-reviewed studies (2015-2025)
- **Comparative Results**: 
  - Technique prevalence analysis (DP, HE, SMPC, TEE)
  - Privacy-utility trade-off visualizations
- **Healthcare Focus**: Compliance assessment with GDPR/HIPAA regulations

## 📂 Repository Structure
```
.
├── analysis/                  # Scripts and outputs
│   ├── thesis.py              # Main analysis script
│   ├── thesis_analysis.py     # Visualization generator
│   ├── results.csv            # Processed study metrics
│   └── *.png                  # Generated figures
├── literature/                # Research materials
│   ├── ThesisTop10Papers.pdf  # Curated studies
│   └── extracted_text.txt     # Processed text data
├── thesis.tex                 # LaTeX source
└── references.bib             # Bibliography
```

## 🔧 Usage
1. Install requirements:
   ```bash
   pip install pandas matplotlib PyPDF2
   ```
2. Run analysis:
   ```bash
   python thesis.py --input ThesisTop10Papers.pdf --output results.csv
   ```

## 📊 Key Findings
- Hybrid (DP+HE) techniques show best privacy-utility balance
- Only 25% of studies address regulatory compliance explicitly
- Computational overhead remains major deployment barrier

## 🎓 Grade & Assessment Summary

The following summarizes the official grading feedback for this thesis (2025):

| Criterion                                  | Max Score | Awarded | Summary |
|---------------------------------------------|-----------|---------|---------|
| **Structure/Presentation**                  | 20        | 16      | Professionally structured; clear sections and figures. Minor text density and formatting inconsistencies, but overall well-organized and readable. |
| **Content**                                | 40        | 30      | Highly relevant topic, thorough literature review and context. Some analysis drifts to description, and more detail on reproducibility and benchmarking is needed. Strong but could link findings to objectives more directly. |
| **Critical Analysis and Evaluation**        | 10        | 7       | Balanced comparison of privacy-preserving methods, with good acknowledgment of trade-offs. Critique of regulatory limitations is present but could be deeper. Recommendations are thoughtful but could be better justified. |
| **Language, Grammar, and Punctuation**      | 10        | 8       | Academic, precise language overall; some minor grammatical errors and overly long sentences. Maintains formal tone and graduate-level competence. |
| **Level of Competency**                     | 10        | 7       | Demonstrates solid grasp of technical and conceptual issues. Practical implementation shown, but deeper evaluation of model security and adversarial threats expected at distinction level. |
| **Referencing (APA 7th Edition)**           | 10        | 5       | Wide range of sources cited, but frequent APA formatting errors, redundant or missing links between text and bibliography. Weakens scholarly presentation and source traceability. |

**Total Score:** 73 / 100

<sup>For detailed examiner comments, see the official result notification.</sup>

## 📜 License
MIT License - See [LICENSE](LICENSE) for details.

## 📍 Reference
If using this work, please cite:  
*Aloho, G.A. (2025). A Critical Analysis... [Master's thesis]. University of East London.*

---

### Key Features:
1. **Thesis-Centric**: Directly mirrors your research objectives/findings
2. **Visual Structure**: Clean file tree matching your actual repository
3. **Actionable**: Includes setup/usage instructions
4. **Academic Ready**: Proper citation prompt and license
5. **Badges**: Professional touch with MIT license shield