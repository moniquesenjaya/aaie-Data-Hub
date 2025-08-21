# AAIE Unified Dataset for AI-Influenced Assignment Submissions

This repository is part of the **Artificial Assessment Intelligence for Educators (AAIE)** capstone project at Deakin University. The goal is to build a high-quality unified dataset that simulates how students use Large Language Models (LLMs) like ChatGPT to complete academic assignments.

---

## Dataset Overview

Each dataset entry includes:
- An assignment prompt and detailed rubric
- Simulated student questions to the LLM
- LLM answers (representing AI support)
- A final student-style essay (Excellent to Poor quality)
- Optional feedback based on the rubric

It is intended to support downstream applications such as:
- LLM fine-tuning and evaluation
- Feedback generation
- Submission quality classification
- Prompt-chain reconstruction

This structure also allows researchers to analyze:
- AI usage patterns in academic writing
- Prompt design and essay development
- The relationship between AI interaction and submission quality

---

## Structure

The dataset is stored in a **JSON file**, where each top-level object represents one assignment prompt. Each entry includes:

- **domain**: Academic field (e.g., Engineering, IT)
- **prompt**: Essay task given to students
- **rubric**: A detailed rubric with multiple criteria and performance descriptors
- **submissions**: A list of essay submissions (Excellent, Good, Average, Need Improvement, Poor)
  - For each submission:
    - `llm_questions`: Simulated student queries to ChatGPT
    - `llm_answers`: Corresponding ChatGPT responses
    - `final_submission`: The final student-like essay
    - `feedback`: Evaluator feedback, per rubric criterion

---

## Folder Structure

```
aaie-data-hub/
├── data/
│   ├── raw/                        # Unstructured or unprocessed files
│   ├── curated/                    # Final JSON files per rubric
│   ├── samples/                    # Sample entries for reference
│   └── schema/                     # Unified JSON schema and validators
│
├── scripts/
│   ├── openai_generation/          # Scripts to generate questions/answers via API
│   ├── quality_generation/         # Scripts to simulate low/high quality answers
│   └── validation/                 # Schema validation tools
│
├── notebooks/                      # Analysis, QA, and visualisation notebooks
│
├── docs/
│   ├── schema_guides/              # Schema documentation
│   ├── public_dataset_research/    # Research on public datasets
│   ├── contributor_guide.md        # Instructions for contributors
│   └── reviewer_guide.md           # Instructions for reviewers
│
├── requirements.txt                # Python dependencies
├── .env.example                    # API key placeholder
├── setup_instructions.md           # How to set up the project
└── README.md                       # You are here
```

---

## Contributions

All contributors are responsible for:

1. Picking a unique `rubric_id` (e.g., `rub_psy_0001`) and filename (e.g., `psych_ms_rub001.json`)
2. Using the provided template and schema
3. Committing to your feature branch, then submitting a PR with:
   - Validation passed 
   - Clean and complete metadata

Refer to [`docs/contributor_guide.md`](./docs/contributor_guide.md) for guidelines on how to contribute.

Refer to [`docs/reviewer_guide.md`](./docs/reviewer_guide.md) for guidelines on how to do peer reviews.

---

## Supported Domains (As of T2 2025)

Essay based assignments are available for the following domains:
- Information Technology
- Engineering
- Psychology
- Accounting
- Teaching

---

## Setup & Validation

See [`setup_instructions.md`](./setup_instructions.md) for environment setup.

---
## Ethics & Safety

All generated content is synthetic. No real student data is used. Rubrics are curated or adapted to ensure ethical and privacy-safe use.

---

## Tools Used

- OpenAI GPT (API)
- Python + JSON
- Jupyter Notebooks (optional)
- Git + GitHub for collaboration

---

## License

To be confirmed.

---

## Maintainers

Led by the **Data Curation Pillar** as part of the AAIE capstone under the School of IT.