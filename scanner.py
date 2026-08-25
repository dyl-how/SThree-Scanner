import subprocess
import json

#drk = input("Enter Directory: ")

result = subprocess.run(
    ["bandit", "-r", "vulnerable_app.py", "-f", "json"],
    capture_output=True,
    text=True
)

output = json.loads(result.stdout)

for error in output['results']:
    print(error)