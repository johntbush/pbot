# Install

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install requests python-dotenv slack-sdk slack-bolt
```

# Setup Tokens

create file called `.env`

ask for keys (these can't be checked into github)

Then place them into file:

```
SLACK_APP_TOKEN="XXX"
SLACK_BOT_TOKEN="YYY"
SLACK_APP_CHANNEL="jb-test"
WEATHER_API_KEY="AAAA"
```

# Start Up the Bot

```
python3 app.py
```

# Resources

Building Bots
https://www.kubiya.ai/resource-post/how-to-build-a-slackbot-with-python
https://tools.slack.dev/bolt-python/getting-started

Accuweather API
https://developer.accuweather.com/apis