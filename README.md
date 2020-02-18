# OKR-chatbot

## Installation (>= 8GB RAM)

- Install python 3.7
- Install pipenv using `pip install pipenv`
- Install rasa, spacy pipeline and other python packages using `pipenv install`

## Pipeline setup

- Download medium sized(md suffix) spacy model `python3 -m spacy download en_core_web_md`
- Run `python -m spacy link en_core_web_md en`

## Stack

![alt text](https://www.lucidchart.com/publicSegments/view/41f6bf32-6af7-432e-bd61-b1e6288c6763/image.png? "stack")

## Commands

- Train RASA using `rasa train`
- Run RASA shell using `rasa shell`
- Run RASA core using `rasa run`
- Run RASA custom actions server using `rasa run actions`

## Environment variables (for deployment only)

- Set `SLACK_BOT_USER_ACCESS_TOKEN` (add in bash profile)

## Testing NLU model

- Train only NLU using `rasa train nlu`
- Run shell using `rasa shell nlu`
- Run e2e tests using `rasa test --stories test_stories.md --e2e` 

## Implemented Conversation Flows

### Create okr
- Person: Create objective
- Bot: Enter title for this objective
- Person: Increase sales
- Bot: Do you want to add a key result for this objective?
- Person: Yes
- Bot: Enter title for the key result
- Person: Increase sales leads/week
- Bot: What is the metric for this key result?
- Person: leads
- Bot: What is the start value for {leads}?
- Person: 20
- Bot: What is the goal value for {leads}?
- Person: 100
- Bot: Key result created successfully. Do you want to add one more?
- Person: No

## Database structure

### user

- id
- slack_id
- workspace_id (TODO)

### objective

- id 
- user_id (user.id)
- title


### keyresult

- id
- title
- start_value
- current_value (TODO)
- goal_value
- objective_id (objective.id)
- user_id (user.id)