import requests

username = input("Enter GitHub username: ")
url = f"https://api.github.com/users/{username}/events"
response = requests.get(url)
event_messages = {
    "PushEvent": "Pushed commits",
    "IssueCommentEvent": "Commented on an issue",
    "PullRequestEvent": "Created a pull request"
}

if response.status_code == 200:
    events = response.json()
    for event in events:
        event_type = event['type']
        message = event_messages.get(event_type, "Unknown activity")
        print(
            f"{message} in {event['repo']['name']} at {event['created_at']}."
        )
else:
    print(f"Error: {response.status_code}")
