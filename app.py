from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
import os
from weather import Weather

load_dotenv()
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
app = App(token=SLACK_BOT_TOKEN)
weather = Weather(WEATHER_API_KEY)


@app.command("/help")
def handle_help_command(ack, body, say):
    ack()
    say("I can help you with the weather forecast and packing list for your trip! Just type `/weather <city> <number of days>` or `/pack <city> <number of days>`")


@app.command("/pack")
def handle_pack_command(ack, body, say):
    ack()


@app.command("/weather")
def handle_weather_command(ack, body, say):
    # Acknowledge the command request
    ack()


def say_forecast(forecast, city, days, say):
    forecast = forecast[:int(days)]
    blocks = []
    blocks.append({
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": f"Forecast for trip to {city.name}, {city.state}"
        }
    })
    for day in forecast:
        blocks.append(
            {"type": "section",
             "text": {"type": "mrkdwn",
                      "text": f"<{day.link}|{day.date_short}> - Min: {day.min_temp}F, Max: {day.max_temp}F, Day: {day.day}, Night: {day.night}"}})
    blocks.append({"type": "divider"})
    say({"blocks": blocks})


# @app.event("app_mention")
# def handle_app_mention_events(body, say):
#     user_id = body.get('event', {}).get('user')
#     say(f"Hey <@{user_id}>!")

@app.message("hello")
def mention_handler(body, say):
    user_id = body.get('event', {}).get('user')
    say(f"Hi <@{user_id}>!")


if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
