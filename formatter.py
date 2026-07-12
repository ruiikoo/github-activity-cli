event_messages = {
    "PushEvent": "Pushed commits",
    "IssueCommentEvent": "Commented on an issue",
    "PullRequestEvent": "Created a pull request"
}


def format_event(event):
    event_type = event["type"]
    message = event_messages.get(event_type, "Unknown activity")

    return (
        f"{message} in {event['repo']['name']} at {event['created_at']}."
    )