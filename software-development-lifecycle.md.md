# Software Dev Lifecycle

- Requirements: A need to be met or problem to be fixed by a piece of software written by the business, a product manager or a client. Written as what should happen, not how to do it (technical).

- Backlog: Requirement turned into trackable task with info about what needs to be done, the priority and who is responsible. Sits in backlog until someone picks it up.

- Development: Dev writes code to implement functionality described by ticket (on a local environment)

- Git Branch: Developers own isolated copy of code to work in, so their changes dont affect shared codebase until everyone is ready

- Pull Request: Developer asking to merge their work (from their branch) into the main codebase. Others can view changes and discuss before committing

- Code Review: Peer-review of proposed changes for bugs or better approaches before approving.

- Automated Testing: Scripts run test cases to check code runs correctly and doesnt break anything else

- Security & Quality Checks: Automated tests used to ensure code is safe from threats or data leaks, as well as making sure performance and code quality is good before deployment

- Deployment: Approved and tested code is released / pushed onto servers and ready to run

- Production: The live environment that real users interact with.

## Questions:

- Why not change prod directly? High risk as a mistake can affect real users directly (no safety net). Also means everyone on the team is familiar and approves of the changes before they are made.

- Why review with another dev? Makes whole team more familiar with codebase, as well as ensuring consistent coding practices. Can also spot mistakes original author didnt find.

- Why are automated tests useful? Human testing can be slow, expensive and contain errors, but automated tests make sure code works correctly every time instantly.

- What happens if insecure code reaches prod? Could damage the company in many ways, exposing them to attacks on the system, data breaches, financial loss and reputation damage.