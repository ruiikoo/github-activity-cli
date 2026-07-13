from github_api import get_user_events
from formatter import format_event

print("""
==============================
    GitHub Activity Viewer
==============================
      """)
username = input("Enter GitHub username: ")
print()

events, status_code = get_user_events(username)

if status_code == 404:
    print(f"Error: GitHub user {username} was not found.")
elif status_code == 403:
    print("Rate limit exceeded. Try again later.")
elif status_code == 500:
    print("GitHub server error.")
elif status_code == 200:
    if not events:
        print(f"No recent activity found for {username}.")
    else:
        number_of_events = len(events)
        print(f"Recent activity for @{username} ({number_of_events} events):")
        
        for event in events:
            print()
            print(format_event(event))
else:
    print(f"GitHub returned status code {status_code}.")