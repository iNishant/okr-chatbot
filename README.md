# OKR-chatbot

## Installation (>= 8GB RAM)

- Install pip3 using `sudo apt-get install python3-pip`
- Install rasa using `pip install rasa-x --extra-index-url https://pypi.rasa.com/simple`
- Install [NLU pipeline dependencies](http://rasa.com/docs/rasa/user-guide/installation/#nlu-pipeline-dependencies)

## Stack

![alt text](https://www.lucidchart.com/publicSegments/view/41f6bf32-6af7-432e-bd61-b1e6288c6763/image.png? "stack")


## Guides

- For slack-rasa integration follow [this](https://rasa.com/docs/rasa/user-guide/connectors/slack/)

## Commands

- Run RASA core using `rasa run`
- Run RASA custom actions server using `rasa run actions`

## Environment variables

- Set `SLACK_BOT_USER_ACCESS_TOKEN` (add in bash profile)