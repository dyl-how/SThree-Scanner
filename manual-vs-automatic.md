# Manual vs Automated Review

## We both found

- Line 18 Hard coded password

- Line 24 Use of eval()

- Line 34 SQL Injection risk

- Line 43 Use of os.system

- Line 48 MD5 hashing

- Line 53 Psuedo Random gen

- Line 74 mktemp as insecure

- Line 90 try execpt pass

## I only found

- Line 19 Hard coded API key (possibly would have if not already flagging as potential password, but not explicitly saying API key)

- Line 59 Users can put in any url (less of an error than what Bandit found so maybe only considered that)

## Bandit only found

- Line 60 verify=False so no security checks on url that user enteredd (didnt find due to unfamiliar with library)

- Line 68 unsafe use of yaml.load, need yaml.safe_load to not initialise arbitrary objects (again im just unfamiliar with library)