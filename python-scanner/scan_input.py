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

    try:
        ruff_result = subprocess.run(
            ["ruff","check",directory,"--output-format","json"],
            capture_output=True,
            text=True
        )
    except FileNotFoundError:
        print("Error: Ruff is not installed or found. try: pip install ruff")

    return bandit_result, ruff_result