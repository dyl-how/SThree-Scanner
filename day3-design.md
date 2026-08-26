# Review

## Flow

- User inputs name of directory

- Bandit scans all of the files in the directory and returns a json output

- Parse output into readable format

- All findings output sequentially

## Questions

- Only the scanning section is specific, so adding another tool would be as simple as adding another results variable that just scans using a different library

- Represented by a Python dictionary with all details from bandit, simplified into a Python object that only contains relevant data

- The only difficult part to maintain would be the parsing of the outputs, if using a different scanner meant the output format would vary slightly