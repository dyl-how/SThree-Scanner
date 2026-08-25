# Requirements

## Severity Levels

- High : directly exploitable code, and likely to cause serious harm (includes previous examples like hard-coded credentials, eval() on raw input or SQL injection risks)

- Medium : A weakness that requires more specific conditions to exploit such as the weak password hashing, where the attacker needs to have access to the hashed data.

- Low : Not currently a risk, but likely to become one in the future due to poor practice / maintainability issues. 

## Program Spec

### Description

This program will analyse a Python project's source code and produce a short report identifying potential security and code quality issues. It is intended to help a dev team quickly locate problems and understand why they are an issue, without manually scanning line by line.

The scanner will focus on common, understood risk patterns and classify each issue found in order of severity so they can be sorted in order of importance.

- Input : User provides file path of the project they want scanned.

- Processing : Scanner reads through .py files in that location, examining each's source code and checking for known risky patterns. Records the error type, where it occurred (file and line), severity, why its a problem and a suggested action for each error.

- Output : A structured report listing findings to be reviewed by a developer. Includes the following fields : 
    - Finding : name of issue detected
    - File : The file where the issue was found
    - Line : The line where the issue was found
    - Severity : High, Medium, or Low to indicate how serious the issue is (see severity levels above)
    - Explanation : Description of why it is a problem
    - Suggested Action : Recommendation on how to fix / mitigate issue
    - Code Snippet : The offending line, shown alongside the finding so the issue can be seen without needing to open the file

#### Example

Finding: Hard-coded password
File: config.py
Line: 18
Severity: HIGH

Explanation:
A password appears to be stored directly in source code. If this file is ever shared, leaked, or made public (including through Git history), the credential is immediately exposed and reusable by anyone who sees it.

Suggested Action:
Store the credential in an environment variable or secrets manager, and load it at runtime instead of hard-coding it.

Code Snippet:
password = "SuperSecret123"
