import os
import subprocess

def get_result(directory):
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return
       
    try:
        bandit_result = subprocess.run(
                ["bandit", "-r", directory, "-f", "json"],
                capture_output=True,
                text=True
            )

    except FileNotFoundError:
        print("Error: Bandit is not installed or found. try: pip install bandit")
        bandit_result = None

    try:
        ruff_result = subprocess.run(
            ["ruff","check",directory,"--output-format","json"],
            capture_output=True,
            text=True
        )
    except FileNotFoundError:
        print("Error: Ruff is not installed or found. try: pip install ruff")
        ruff_result = None

    return bandit_result, ruff_result

# could modify so that test can run with just one of the scanners if other is working fine?????