import requests

apiEndpoint = 'https://okr-chatbot.herokuapp.com/v1/graphql'
debug = True


def log(*argv):
    if not debug:
        return
    print("\n")
    for arg in argv:
        print(arg, end="")


def getUserFromSlackId(slackId):
    # returns status and email
    # sender id for shell is "default"
    # database has entry for slack_id "default"
    # first check if user with slack id exists
    jsonData = {
        'query': '''{
            user(where: {slack_id: {_eq: "%s"}}) {
              id
              slack_id
              updated_at
              created_at
            }
          }''' % slackId,
    }
    log("getting user from slack id: ", slackId)
    req = requests.post(url=apiEndpoint, json=jsonData)
    if req.status_code != 200:
        return (False, None)
    users = req.json()['data']['user']
    if len(users):  # user with slack id exists
        return (True, users[0])
    # create user with given slack id
    jsonData = {
        'query': '''mutation {
            insert_user(objects: {slack_id: "%s"}) {
              returning {
                created_at
                id
                slack_id
                updated_at
              }
            }
          }
        ''' % slackId
    }
    req = requests.post(url=apiEndpoint, json=jsonData)
    if req.status_code != 200:
        return (False, None)
    return (True, req.json()['data']['insert_user']['returning'][0])


def createNewObjective(objective, user_id):
    # returns status and objective
    log("creating new objective: ", objective)
    jsonData = {
        'query': '''mutation {
            insert_objective(objects: {title: "%s", user_id: "%s"}) {
              returning {
                id
                title
                created_at
                updated_at
                user_id
              }
            }
          }
        ''' % (objective, user_id)
    }
    req = requests.post(url=apiEndpoint, json=jsonData)
    if req.status_code != 200:
        return (False, None)
    return (True, req.json()['data']['insert_objective']['returning'][0])


def createNewKeyResult(
        kr_title, kr_start_value, kr_goal_value, objective_id, user_id):
    log("creating new kr: ", kr_title)
    jsonData = {
        'query': '''mutation {
            insert_keyresult(objects: {objective_id: "%s", start_value: "%s",
            title: "%s", user_id: "%s", goal_value: "%s"}) {
              returning {
                id
                objective_id
                start_value
                title
                updated_at
                user_id
                goal_value
                created_at
              }
            }
          }
        ''' % (objective_id, kr_start_value, kr_title, user_id, kr_goal_value)
    }
    req = requests.post(url=apiEndpoint, json=jsonData)
    if req.status_code != 200:
        return (False, None)
    return (True, req.json()['data']['insert_keyresult']['returning'][0])
