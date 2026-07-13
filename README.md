## GitHub User Activity Tracker CLI

## Rpoject page URL:
https://roadmap.sh/projects/github-user-activity

## Description:
This is a CLI application that retrieves and displays recent GitHub activity for any public GitHub user using the GitHub Events API.

## Features:
- Fetches GitHub user events;
- Displays repository information;
- Formats timestamps to readable format;
- Handles API errors;
- Handles users with no activity;
- Modular code structure.

## Technologies Used:
- Python;
- Requests library;
- GitHub REST API;
- Git.

## For installation run the commands below in the corresponding sequence:
```bash
git clone https://github.com/ruiikoo/github-activity-cli.git
cd github-activity-cli

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

## To run the app:
```bash
python main.py
```
Type in the GitHub 'username' you want to get the recent activity of.

## Example:
Input:
```bash
Enter GitHub username: torvalds
```
Output:
```bash
Recent activity for @torvalds (30 events):

• Pushed commits
  Repository: torvalds/linux
  Time: Jul 12, 2026 19:32 UTC
```

## Project Structure:
```bash
github_activity/
│
├── main.py          # Application entry point
├── github_api.py    # GitHub API communication
├── formatter.py     # Event formatting logic
├── requirements.txt # Dependencies
└── .gitignore       # Ignored files
```
