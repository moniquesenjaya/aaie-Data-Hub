# AAIE JSON File Schema Reference

This document outlines the required structure and fields for every curated JSON dataset file used in the AAIE project. It serves as a reference for contributors to understand the format, avoid schema errors, and ensure data consistency across all entries.

---

## File Structure Overview

Each JSON file must contain:

| Key           | Type     | Description |
|---------------|----------|-------------|
| `domain`      | `string` | Academic domain (e.g., "IT", "Psychology", "Engineering") |
| `prompt`      | `string` | The essay or assignment question given to students |
| `rubric`      | `object` | Rubric used to evaluate submissions (see below) |
| `submissions` | `array`  | Five or more submissions representing different quality bands (Excellent → Poor) |

---

## Rubric Structure

### Required Format

```json
"rubric": {
  "rubric_id": "rub_domain_0001",
  "criteria": [ ... ]
}
```

Each `criterion` inside `criteria` must include:

| Field                    | Type     | Description |
|-------------------------|----------|-------------|
| `criterion_id`          | `string` | Unique ID for the criterion (e.g., "c1", "c2") |
| `name`                  | `string` | Criterion title |
| `description`           | `string` | What this criterion evaluates |
| `performance_descriptors` | `object` | Text descriptors for each performance level |

### Required Performance Bands

Each `performance_descriptors` must contain:

- `excellent`
- `good`
- `average`
- `needs_improvement`
- `poor`

Example:

```json
{
  "criterion_id": "c1",
  "name": "Understanding of Theory",
  "description": "Demonstrates understanding of theoretical concepts.",
  "performance_descriptors": {
    "excellent": "Demonstrates deep insight...",
    "good": "Correct understanding...",
    "average": "Somewhat accurate...",
    "needs_improvement": "Superficial explanation...",
    "poor": "Lacks understanding..."
  }
}
```

---

## Submissions Structure

Each JSON must include at least **five submissions**, one per quality level:

```json
"submissions": [
  {
    "quality": "Excellent",
    "key_points": [...],
    "llm_questions": [...],
    "llm_answers": [...],
    "final_submission": "...",
    "feedback": {
      "c1": "...",
      "c2": "...",
      ...
    }
  },
  ...
]
```

### Required Fields per Submission:

| Field              | Type      | Description |
|-------------------|-----------|-------------|
| `quality`         | `string`  | One of: `Excellent`, `Good`, `Average`, `Needs Improvement`, `Poor` |
| `key_points`      | `array`   | Bullet-point summary of student’s main ideas |
| `llm_questions`   | `array`   | Prompts the student might ask an LLM |
| `llm_answers`     | `array`   | LLM's answers to those prompts |
| `final_submission`| `string`  | The student's final AI-influenced submission |
| `feedback`        | `object`  | Feedback comments aligned with rubric `criterion_id`s |

### Feedback Requirements

- Each `submission.feedback` must contain keys that match **every `criterion_id`** in the rubric.

---

## Common Errors to Avoid

- Missing top-level keys (`domain`, `prompt`, `rubric`, `submissions`)
- Not providing all 5 `performance_descriptors`
- Using incorrect casing for `quality` values (`Excellent`, not `excellent`)
- Mismatched feedback: `criterion_id` in rubric not reflected in `feedback`
- Less than 5 total submissions in the `submissions` array

---

## Naming Convention

- The `rubric_id` must follow the format: `rub_domain_####`  
  Example: `"rub_psychology_0001"`
- The **JSON file name must match the `rubric_id`**, e.g.:

```
rub_psychology_0001.json
rub_it_0003.json
```

---

## Example File

> A complete sample file is provided in `samples/sample_dataset1.json`.

---

## Tips for Contributors

- Use the provided `validation.py` script to catch issues before pushing.
- Run `python scripts/validation/validation.py` before submitting a pull request.
- Follow naming conventions: `rubric_id` should be unique (e.g., `"rub_psychology_0001"`, `"rub_it_0003"`)

---

_For questions or inconsistencies, reach out to the Data Curation Lead or check `contributor_guide.md`._