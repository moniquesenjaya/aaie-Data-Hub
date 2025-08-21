# Contributor Guide (Data Curation Team)

Welcome to the AAIE Data Curation team! This guide outlines how to contribute to the project effectively. Whether you're submitting documentation, a JSON dataset, a Python script, or a Jupyter notebook this guide is for you.

---

## What You Can Contribute

You can contribute the following types of files:

### Markdown Documentation (`.md`)
- Setup or instruction guides
- Schema explanations
- Public dataset research
- Documentation for scripts or notebooks
- Contributor or review guidelines

### JSON Dataset Files
- One file per rubric/assignment
- Must follow the unified schema (see `/data/schema/`)
- Must include at least 5 submission with all quality levels (Excellent → Poor)

### Python Scripts (`.py`)
- Automation for prompt generation, validation, file formatting
- Utility tools to help curate or manage the dataset

### Jupyter Notebooks (`.ipynb`)
- Data exploration
- QA pipelines
- Visualisation and statistics

---

## Contribution Workflow

### 1. Make Sure You're Set Up
Follow the [`setup_instructions.md`](../setup_instructions.md) to fork, clone, and set up your environment.

---

### 2. Create a New Branch

Always branch off the latest `development` branch from upstream:

```bash
git fetch upstream
git checkout -b your-branch-name upstream/development
```

Use a short and clear name, like `fix-json-validation` or `add-rubric-psychology`.

---

### 3. Add Your Contribution

- For documentation: add your `.md` file in the appropriate `docs/` folder
- For dataset JSON: place your file in `data/curated/` if it's complete, or `data/raw/` if it's unprocessed
- For scripts: place Python tools in `scripts/` (under a relevant subfolder)
- For notebooks: save under `notebooks/` and clearly name the purpose

---

### 4. Validate Your Work

If you're submitting a JSON file make sure:
- Schema is followed
- File is named correctly
- No missing or extra fields

---

### 5. Commit and Push

```bash
git add .
git commit -m "Short message describing your change"
git push origin your-branch-name
```

---

### 6. Open a Pull Request (PR)

1. Go to your forked repo on GitHub
2. Click **"Compare & pull request"**
3. Set base repo as `InnovAIte-Deakin/aaie-data-hub` and base branch as `development`
4. Fill in the title and description using the PR template
5. Request 2 peer reviews and 1 senior reviewer

---

### 7. Wait for Reviews

Refer to [`docs/reviewer_guide.md`](./docs/reviewer_guide.md) for guidelines on how to do peer reviews.

---

Thank you for your contribution! Your work helps build a high-quality educational dataset for research and AI development.