## GitHub User Activity Tracker CLI

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

## Clone the repository and install the dependencies:
git clone <repository-url>
cd github_activity

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

## To run the app:
python main.py
Type in the GitHub 'username' you want to get the recent activity of.

## Example:
Input:
Enter GitHub username: torvalds

Output:
Recent activity for @torvalds (30 events):

• Pushed commits
  Repository: torvalds/linux
  Time: Jul 12, 2026 19:32 UTC

## Project Structure:
github_activity/
│
├── main.py          # Application entry point
├── github_api.py    # GitHub API communication
├── formatter.py     # Event formatting logic
├── requirements.txt # Dependencies
└── .gitignore       # Ignored files