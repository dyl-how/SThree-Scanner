# Day 4 Review

- Most findings make sense, although some from previous days are missing due to different errors on the same line being ignored by my dedup algorithm

- Clean app still has some problems, mainly in the style of coding scan, due to unsorted imports, but some security risks associated with subprocess module, but this is needed as a replacement to the previous use of blind os commands running.

## AI System Explanation

- Not implemented yet but still thought I should write up a design process

- Send external API the Issue object containing all the info about the problem (including a code snippet from Bandit to allow for more relevant explanation given context). Only this small section is sent as to not reveal full source code. Use a try/except structure to account for any faliure on part of the API or the AI model being down. Usual suggested_action field still included in case AI is not helpful, or down and flags an error