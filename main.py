from github_api import get_user_events
from formatter import format_event

username = input("Enter GitHub username: ")

events = get_user_events(username)

if events is None:
    print("Error: Unable to fetch GitHub activity.")
elif not events:
    print(f"No recent activity found for {username}.")
else:
    for event in events:
        print(format_event(event))