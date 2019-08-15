# OKR-chatbot

## Installation (>= 8GB RAM)

- Install python3
- Install pip3 using `sudo apt-get install python3-pip`
- Install rasa, spacy pipeline and other python packages using `pip3 install -r requirements.txt`

## Pipeline setup

- Download medium sized(md suffix) spacy model `python3 -m spacy download en_core_web_md`
- Run `python -m spacy link en_core_web_md en`

## Stack

![alt text](https://www.lucidchart.com/publicSegments/view/41f6bf32-6af7-432e-bd61-b1e6288c6763/image.png? "stack")


## Guides

- For slack-rasa integration follow [this](https://rasa.com/docs/rasa/user-guide/connectors/slack/)

## Commands

- Train RASA using `rasa train`
- Run RASA shell using `rasa shell`
- Run RASA core using `rasa run`
- Run RASA custom actions server using `rasa run actions`

## Environment variables

- Set `SLACK_BOT_USER_ACCESS_TOKEN` (add in bash profile)

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