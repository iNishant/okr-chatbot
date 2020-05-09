#!/bin/bash
git clone https://github.com/iNishant/okr-chatbot.git
cd okr-chatbot/rasa
sudo apt-get update
sudo apt-get install python3-pip -y
pip3 install -r requirements.txt
python3 -m spacy download en_core_web_md
python3 -m spacy link en_core_web_md en