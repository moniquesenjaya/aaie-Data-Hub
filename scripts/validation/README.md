# Validation Script and CI Workflow

This folder contains the dataset validation script used in the AAIE Unified Dataset project. The script ensures that all `.json` files in `data/curated/` comply with the expected schema, naming conventions, and domain alignment.

This script is also integrated with GitHub Actions to automatically validate data submissions during development.

---

## Purpose

To enforce data consistency and correctness before contributions are merged into the project. This includes:

- Schema validation
- Filename and rubric ID matching
- Domain and rubric ID alignment
- Formatting conventions

---

## Key Validation Rules

1. **Schema Validation**  
   All files must comply with `data/schema/schema.json` using JSON Schema Draft-07.

2. **rubric_id Format**  
   Must match the pattern: `rub_<domain>_<4-digit>` (e.g., `rub_psychology_0001`)

3. **Filename Match**  
   Filename must match the `rubric_id`.  
   Example: `rub_psychology_0001.json` must contain `"rubric_id": "rub_psychology_0001"`

4. **Domain Match**  
   - The `domain` field must match the domain segment in `rubric_id` (case-insensitive).
   - Special Case: If `domain` is `"Information Technology"`, the rubric ID must be like `rub_it_0001`

5. **rubric_id Casing**  
   Must be all lowercase.

---

## How to Run Manually

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Validate a Single File

```bash
python scripts/validation/validation.py data/curated/rub_psychology_0001.json
```

### Validate All Files

```bash
python scripts/validation/validation.py data/curated
```


---

## GitHub Actions CI Integration

The validation script runs automatically on push to any branch in a forked repository.

**Workflow file**: `.github/workflows/validate-json.yml`

**Trigger:** Push to any branch that changes:

- `data/curated/*.json`
- `scripts/validation/validate_json.py`
- `data/schema/schema.json`
- `requirements.txt`
- The workflow file itself

If validation fails, the CI check will fail and display all detected issues in the GitHub Actions log.

---

## Sample Test Cases and How to Fix

### Valid Example

Filename: `rub_psychology_0001.json`

```json
{
  "domain": "Psychology",
  "rubric": {
    "rubric_id": "rub_psychology_0001"
  }
}
```

### Case 1: Filename Mismatch

**Filename:** `rub_psych_0001.json`  
**rubric_id:** `"rub_psychology_0001"`

**Error:** Filename does not match rubric_id  
**Fix:** Rename file to `rub_psychology_0001.json`

---

### Case 2: rubric_id Not Lowercase

**rubric_id:** `"rub_Psychology_0001"`

**Error:** rubric_id must be all lowercase  
**Fix:** Change to `"rub_psychology_0001"`

---

### Case 3: Domain Mismatch

```json
"domain": "Psychology",
"rubric": {
  "rubric_id": "rub_sociology_0001"
}
```

**Error:** Domain mismatch  
**Fix:** Update rubric_id to `"rub_psychology_0001"`

---

### Case 4: Information Technology Domain

```json
"domain": "Information Technology",
"rubric": {
  "rubric_id": "rub_information_technology_0001"
}
```

**Error:** rubric_id must be `rub_it_####`  
**Fix:** Change rubric_id to `"rub_it_0001"`

---
### Case 5: Missing Required Field (llm_answers)

```json
{
  "submissions": [
    {
      "quality": "Excellent",
      "key_points": ["Explains cognitive bias"],
      "llm_questions": ["What is confirmation bias?"],
      "final_submission": "This is the final essay.",
      "feedback": {
        "c1": "Strong explanation"
      }
    }
  ]
}
```

**Error:** Submission 1 missing field: llm_answers  
**Fix:** Add the `llm_answers` field as an array of LLM responses.

---

### Case 6: Missing Feedback Object

```json
{
  "submissions": [
    {
      "quality": "Good",
      "key_points": ["Explains biases"],
      "llm_questions": ["What is anchoring bias?"],
      "llm_answers": ["Anchoring bias refers to..."],
      "final_submission": "This is a sample essay."
    }
  ]
}
```

**Error:** Submission 1 missing field: feedback  
**Fix:** Add a `feedback` field, even if empty or partial. Example:

```json
"feedback": {
  "c1": "Clear explanation",
  "c2": "Needs more detail"
}
```

---

### Case 7: Invalid Quality Label

```json
{
  "quality": "Perfect"
}
```

**Error:** Submission 1 has invalid quality label: Perfect  
**Fix:** Use one of: Excellent, Good, Average, Needs Improvement, Poor

---

### Case 8: Extra Field Not Allowed

```json
{
  "domain": "Psychology",
  "prompt": "Explain biases",
  "extra_field": "should not be here"
}
```

**Error:** Additional properties not allowed  
**Fix:** Remove any fields not defined in the schema

---

## Tips for Contributors

- Always run the validator locally before pushing
- Make sure your rubric ID follows the naming convention
- Use the correct domain spelling and casing
- Push to your forked repo to see validation via GitHub Actions

---

