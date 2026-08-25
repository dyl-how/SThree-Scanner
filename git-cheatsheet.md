# Git Cheatsheet

Git is used for version control, tracking and allowing changes to a projects files over time, who made them and why. A repo is the actual project folder, plus its history of changes. 

Used to save the history of a projects (meaning you can rollback if something breaks), allows collaboration between devs via isolated branches which are then merged, and lets anyone see who made a change and a description of why they made it.

## Commands

### Setup

- git clone [url] : downloads copy of the repo linked locally

- git status : see what is changed and staged

### Common workflow

- git add [file]
- git add .      : both used to stage files, either specifically named or all changed files

- git commit -m "message" : save staged changes to local repo with description

- git push : uploads commits to remote repo

- git pull : download and merge other's changes into local repo

### Branching

- git branch : lists branches
- git branch [name] : create new branch

- git checkout [name] : switch to new branch
- git checkout -b [name] : creates and switches to a new branch in one step

- git merge [name] : merge another branch into your current one

### Inspecting

- git log : view commit history

- git diff : see line-by-line changes not yet staged

