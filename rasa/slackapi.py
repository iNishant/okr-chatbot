import requests
import os


def getUserEmailFromUserID(userId):
    # returns status and email
    defaultSenderId = "default"
    if userId == defaultSenderId:
        return (True, "test@example.com")
    ## make slack user info API call
    ## TODO: have some caching mechanism, slack api has rate limits
    slack_token = os.environ['SLACK_BOT_USER_ACCESS_TOKEN']
    reqUrl = 'https://slack.com/api/users.info?token=' + slack_token + '&user=' + userId
    resp = requests.get(reqUrl)
    if resp.status_code == 200:
        userEmail = resp.json()['user']['profile']['email']
        return (True, userEmail)
    else:
        return (False, "Slack API error")

