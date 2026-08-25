This program will analyse a Python project's source code and produce a short report identifying potential security and code quality issues. 
It is intended to help a dev team quickly locate problems and understand why they are an issue, without manually scanning line by line.

The scanner will focus on common, understood risk patterns and classify each issue found in order of severity so they can be sorted in order of importance.

- Input : User provides file path of the project they want scanned.

- Processing : Scanner reads through .py files in that location, examining each's source code and checking for known risky patterns.
                Records the error type, where it occurred (file and line), severity, why its a problem and a suggested action for each error.

- Output : A structured report listing findings to be reviewed by a developer. Includes the following fields :
-   Finding : name of issue detected
-   File : The file where the issue was found
-   Line : The line where the issue was found
-   Severity : High, Medium, or Low to indicate how serious the issue is (see severity levels above)
-   Explanation : Description of why it is a problem
-   Suggested Action : Recommendation on how to fix / mitigate issue
-   Code Snippet : The offending line, shown alongside the finding so the issue can be seen without needing to open the file



### Day 2 version

Scans a given directory for python files and returns a terminal output of information on the locations and types of  security / coding issues that it detects

Requires Bandit library to be installed as this is used to read the files and find the issues. This can be installed using pip install bandit within the same environment as the python file when it runs

Run in terminal in the environment with bandit by python scanner.py, followed by the name of the directory you wish to scan when prompted

Expect a short section of text with labelled info for each issue found.
