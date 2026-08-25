import subprocess
import json
import os

# Add lookup table for types of error and suggested action

class Issue:
    def __init__(self, error_dict):
        self.finding = error_dict['test_name']
        self.file = error_dict['filename']
        self.line = error_dict['line_number']
        self.sev = error_dict['issue_severity']
        self.explanation = error_dict['issue_text']
        self.code = error_dict['code']

    def __str__(self):
        return (
            f"[{self.sev}] {self.finding}\n"
            f"  File: {self.file}, Line: {self.line}\n"
            f"  {self.explanation}\n"
            f"  Code:\n{self.code}"
        )


def main():

    directory = input("Enter Directory: ")
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return


    try:
        result = subprocess.run(
            ["bandit", "-r", directory, "-f", "json"],
            capture_output=True,
            text=True
        )

    except FileNotFoundError:
        print("Error: Bandit is not installed or found. try: pip install bandit") 

    output = json.loads(result.stdout)

    errors = []

    if output['metrics']['_totals']['loc'] == 0:
        print(f'No python files found in {directory}')

    elif not output['results']:
        print('No issues found.')
    else:
        for error in output['results']:
            errors.append(Issue(error))
            print(Issue(error))


main()