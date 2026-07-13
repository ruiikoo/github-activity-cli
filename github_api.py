import requests

def get_user_events(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json(), response.status_code
    else:
        return None, response.status_code