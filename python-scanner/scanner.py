import scan_input
import json
import scan_parse
import dedup

# Add lookup table for types of error and suggested action

# Ruff problems - No code or severity within json



def write_report(findings, filepath):
    data = [f.to_dict() for f in findings]
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

def main():

    directory = input("Enter Directory: ")
    b_result, r_result = scan_input.get_result(directory)

    if not b_result or not r_result:
        return
    try:
        b_output = json.loads(b_result.stdout)
        r_output = json.loads(r_result.stdout)
    except json.JSONDecodeError:
        print("Failed to extract json output")
        return

    errors = []

    high = []
    med = []
    low = []

    if b_output['metrics']['_totals']['loc'] == 0:
        print(f'No python files found in {directory}')

    if not b_output['results']:
        print('No issues found with Bandit.')
    else:
        for error in b_output['results']:
            errors.append(scan_parse.parse_bandit(error))

    if not r_output:
        print("No issues found by Ruff")
    else:
        for error in r_output:
            errors.append(scan_parse.parse_ruff(error))




    unique_errors = dedup.deduplicate(errors)

    write_report(unique_errors, "report.json")

    for issue in unique_errors:
        if issue.sev == "HIGH":
            high.append(issue)
        elif issue.sev == "MEDIUM":
            med.append(issue)
        elif issue.sev == "LOW":
            low.append(issue)

    print("\nSCAN COMPLETE")

    print(f"\n{len(b_output['metrics']) - 1} files scanned.")

    print(f"\n{len(unique_errors)} findings.")
    print(f"\n{len(high)} high risk findings.")
    print(f"{len(med)} medium risk findings.")
    print(f"{len(low)} low risk findings.")

    print("\nUNIQUE FINDINGS:")
    for issue in unique_errors:
        print("-------------------------")
        print(issue)

if __name__ == "__main__":
    main()