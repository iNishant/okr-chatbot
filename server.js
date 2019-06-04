const express = require("express");
const bodyParser = require("body-parser");
const request = require("request");

const app = express();
const port = 3000;
const BOT_TOKEN = process.env.OKR_BOT_TOKEN;

app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

function slackAPIVerifier(req, res) {
  // needs to respond back with same challenge
  let challenge = 'Hello world'; // some random message
  if (req.body && req.body.challenge) challenge = req.body.challenge;
  res.send({ challenge });
}

function sendSlackMessage(body, channel, token) {
  const data = {
    text: body,
    channel: channel,
  };
  var options = {
		method: "POST",
	  url: "https://slack.com/api/chat.postMessage",
	  body: JSON.stringify(data),
	  headers: {
	    'Authorization': `Bearer ${token}`,
	    'Content-Type': 'application/json',
	  },
  };
  request(options, (error, response, body) => {
    // console.log(body);
	});
}

function messageEventHandler(req, res) {
  const body = req.body;
  if (
    body.event
    && body.event.type === 'message' // message event
    && body.event.channel_type === 'im' // direct messages to bot
    && body.event.subtype !== 'bot_message' // ignore bot messages
  ) {
    // direct message to bot
    const channel = body.event.channel;
    sendSlackMessage(
      "Hello from our backend",
      channel,
      BOT_TOKEN,
    );
    res.send();
  } else {
    slackAPIVerifier(req, res);
  }
}

app.post('/', messageEventHandler);

app.get('/', slackAPIVerifier);

app.listen(
  port,
  () => console.log(`Listening on port ${port}`),
);
