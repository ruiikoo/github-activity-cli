from datetime import datetime

event_messages = {
    "PushEvent": "Pushed commits",
    "IssueCommentEvent": "Commented on an issue",
    "PullRequestEvent": "Created a pull request"
}


def format_event(event):
    event_type = event["type"]
    message = event_messages.get(event_type, "Unknown activity")
    date = datetime.strptime(event["created_at"], "%Y-%m-%dT%H:%M:%SZ")
    formatted_date = date.strftime("%b %d, %Y %H:%M UTC")

    return f"""• {message}
  Repository: {event['repo']['name']}
  Time: {formatted_date}"""