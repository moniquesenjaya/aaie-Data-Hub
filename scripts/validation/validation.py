import os
import sys
import json
import glob
from jsonschema import validate, ValidationError
from jsonschema.exceptions import SchemaError

# Path to the JSON Schema file (adjust if needed)
SCHEMA_PATH = "data/schema/schema.json"

def load_schema():
    """
    Load the JSON Schema from disk.
    """
    try:
        with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Could not load schema: {e}")
        sys.exit(1)

def validate_filename_vs_rubric(file_path, rubric_id):
    """
    Ensure that the filename matches the rubric_id (e.g., rub_psychology_0001.json)
    """
    filename = os.path.basename(file_path)
    expected_name = rubric_id + ".json"
    return filename == expected_name

def extract_domain_from_rubric_id(rubric_id):
    """
    Extract the domain part from rubric_id formatted as rub_<domain>_<####>
    """
    parts = rubric_id.split("_")
    if len(parts) >= 3:
        return "_".join(parts[1:-1])  # handles rub_data_science_0001
    return ""

def validate_json(file_path, schema):
    """
    Validate a single JSON file against the schema and additional rules.
    Returns a list of error messages (empty if valid).
    """
    errors = []

    # Load the JSON file
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        errors.append(f"\nFile: {file_path}\nIssue: JSON loading error\nDetails: {e}")
        return errors

    # Validate against the JSON Schema
    try:
        validate(instance=data, schema=schema)
    except ValidationError as ve:
        errors.append(
            f"\nFile: {file_path}\nIssue: Schema validation failed\nDetails: {ve.message}"
        )
    except SchemaError as se:
        errors.append(f"\nFile: {file_path}\nIssue: Invalid schema file\nDetails: {se}")
        return errors

    # Extract fields for custom checks
    rubric_id = data.get("rubric", {}).get("rubric_id", "")
    domain = data.get("domain", "")

    # Check rubric_id starts with rub_
    if not rubric_id.startswith("rub_"):
        errors.append(
            f"\nFile: {file_path}\nIssue: rubric_id must start with 'rub_'\nFound: '{rubric_id}'"
        )

    # Check filename matches rubric_id
    if rubric_id and not validate_filename_vs_rubric(file_path, rubric_id):
        errors.append(
            f"\nFile: {file_path}\nIssue: Filename mismatch\n"
            f"Expected filename: {rubric_id}.json"
        )

    # Check that rubric_id is all lowercase
    if rubric_id and not rubric_id.islower():
        errors.append(
            f"\nFile: {file_path}\nIssue: rubric_id must be all lowercase\n"
            f"Found: '{rubric_id}'"
        )

    # Extract domain part from rubric_id
    rubric_domain = extract_domain_from_rubric_id(rubric_id)
    domain_normalised = domain.strip().lower()

    # Special rule for Information Technology → 'it'
    if domain_normalised == "information technology":
        if rubric_domain != "it":
            errors.append(
                f"\nFile: {file_path}\nIssue: Domain mismatch\n"
                f"Domain is 'Information Technology', so rubric_id should be 'rub_it_####'\n"
                f"Found rubric_id: '{rubric_id}'"
            )
    else:
        # All other domains must match case-insensitively
        if rubric_domain != domain_normalised:
            errors.append(
                f"\nFile: {file_path}\nIssue: Domain mismatch\n"
                f"Expected domain in rubric_id: '{domain_normalised}'\n"
                f"Found domain in rubric_id: '{rubric_domain}'"
            )



    return errors

def validate_all_jsons_in_folder(folder):
    """
    Validate all .json files in a specified folder.
    Returns a list of all validation errors found.
    """
    schema = load_schema()
    all_errors = []

    json_files = glob.glob(os.path.join(folder, "*.json"))
    for file_path in json_files:
        errors = validate_json(file_path, schema)
        if errors:
            all_errors.extend(errors)

    return all_errors

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validation.py <file_or_folder>")
        sys.exit(1)

    path = sys.argv[1]

    if os.path.isdir(path):
        errors = validate_all_jsons_in_folder(path)
    else:
        schema = load_schema()
        errors = validate_json(path, schema)

    if errors:
        print("\nValidation failed with the following issues:")
        for err in errors:
            print(err)
        sys.exit(1)
    else:
        print("All validations passed.")
        sys.exit(0)
