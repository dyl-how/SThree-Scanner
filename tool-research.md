# Tool Research

## 1 - Bandit

- What it does : Analysis tool to find common security issues by parsing code and checking against a set of built in rules.

- Install : pip install bandit within a virtual environment

- Run : bandit [filename] for one file, bandit -r [path] for directory

- What it detects : "Common security issues", unsure if this included poor maintainability, will have to check

- Machine-readable : allows user to choose output format (csv, json, custom etc)

- Advantages : easy to set up and run and almost exactly fits the project outline, will have to test on vulnerable code to see if it works



## 2 - Ruff

- What it does : Python linter and code formatter, verifying the style of a piece of code over its function

- Install : pip install ruff within virtual environment

- Run : ruff check to lint and ruff format to format from command line

- What it detects : Simple security errors, but mainly coding standards to ensure maintainable and readable code

- Machine-readable : allows for json output

- Advantages : very fast (written in rust) and works with many other libraries to find best code formats / standards to enforce

- Limitations : Not as security focussed as bandit, so some security issues may go unnoticed in favour of formatting problems, which are also important, but less urgent to be fixed.


## 3 - Semgrep

- What it does : Used to detect bugs, vulnerabilities and security standards slipping within your code, but rules are written in a readable syntax that looks like the code is searching for unlike Bandit, which has a fixed ruleset based on python security

- Install : pip install semgrep

- Run : semgrep scan [file] uses base community ruleset, but can modify using --config

- What it detects : depends entirely on your chosen ruleset, so can be whatever you want it to be, or a premade community ruleset if you want it to be simpler

- Machine-readable : Yes as it is built for integrating into other tools, and so very customisable

- Advantages : Very flexible to whatever problems you want, as well as other things that make it fit very easily into whatever porject you want it to

- Limitations : Much more complicated to set up (need to define ruleset), and so steeper learning curve to get working, making it harder to integrate than the other two options

## Decision

I will use Bandit as it seems to be the one that is most in line with what I want to create and is also simplest to set up and run.