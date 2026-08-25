# Manual Review of vulnerable code

- Lines 18 and 19: Hard coded credentials (password and API key) thta could be leaked if codebase leaked

- Line 24: Use of eval() allows for attackers to inject harmful code

- Line 34: Concatenated raw user input to SQL statement allowing for SQL injection

- Line 43: Allows raw user input to be run directly into the shell, and characters like ; let attacker chain commands with whatever permissions the python program has

- Line 48: Uses MD5 hashing (not effective for securing passwords)

- Line 53: random.randint() is not truly random so attackers can find tokens

- Lines 59: Allows user to input any url, possible harmful sites included

- Line 74: mktemp() creates a temporary file to act as storage, but will be used in this case to contain sensitive data in plain text

- Line 90: Passes on any error without explaining creating a code maintaiability issue as its unclear what went wrong.