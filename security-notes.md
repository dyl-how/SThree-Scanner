# Security Notes

## Hard-coded Credentials

- Dangerous: Passwords stored in plaintext directly in source code which anyone with access to the repo can view (also if deleted, can view in commit history)

- What attacker can do: If repo is leaked, they can see credentials immediately and log into whatever system is locked behind it

- How to make safer: Store credentials in environment variables that are loaded at runtime, rather than committing them to a repo.

## eval()

- Dangerous: executes string as actual Python code, meaning if it takes user input, user cna put whatever code they want

- What attacker can do: Enter code that could be harmful to system, reveal sensitive data, or grant a connection back to their own computer (backdoor)

- How to make safer: Avoid using eval on user input, or at least heavily sanitise user input beforehand. 

## SQL from user input

- Dangerous: Risks SQL injection if user input is not sanitised.

- What attacker can do: Enter SQL to change logic of statement, returning entire tables of data, or chaining commands to modify / delete data

- How to make safer: Sanitise user input or use prepared statements to handle value checking rather than string concatenation

## OS commands

- Dangerous: passes user input directly to the OS command line, so similar to eval() but at OS level (higher risk)

- What attacker can do: chain extra commands to read, modify, or delete files, or install files like malware

- How to make safer: Avoid passing raw user input into shell commands

## Weak hashing

- Dangerous: Using outdated algorithms (like MD5) can be vulnerable to modern brute force techniques, due to collisions and its speed

- What attcker can do: if they gain access to the database of hashed passwords, they can crack weak ones very quickly.

- How to make safer: use a better hashing algorithm designed for passwords.