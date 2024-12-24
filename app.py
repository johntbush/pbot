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
    user_id = body["user_id"]
    if len(body["text"].split(" ")) != 2:
        say(f"<@{user_id}>, please enter a city and number of days")
        return
    city, days = body["text"].split(" ")
    if not days.isdigit() or int(days) < 1 or int(days) > 5:
        say(f"<@{user_id}>, please enter a valid number of days (1-5)")
        return
    city = weather.get_location(city)
    if city:
        forecast = weather.get_forecast(city.key)

        packing_list = ['tent', 'sleeping bag', 'sleeping pad', 'water bottle', 'clothes', 'first aid kit',
                        'flashlight']
        under_60 = False
        under_40 = False
        under_30 = False
        over_80 = False
        precipitation = False
        notes = []
        for day in forecast:
            if day.precipitation:
                precipitation = True
            if day.min_temp < 60:
                under_60 = True
            if day.min_temp < 30:
                under_30 = True
            if day.min_temp < 40:
                under_40 = True
            if day.max_temp > 80:
                over_80 = True

        if precipitation and not under_30:
            notes.append(f"Looks like its going to rain! Make sure to bring rain gear!")
            packing_list.append('rain gear')
        if precipitation and under_30:
            notes.append(f"Looks like its going to rain and maybe even snow! Be prepared! :snowman:")
            packing_list.append('rain gear')
            packing_list.append('snow shovel')
        if under_60:
            packing_list.append('lightweight jacket')
            packing_list.append('pants')
        if under_40:
            notes.append(f"Brr, its going to be cold! :cold_face: Make sure to bring a :coat: and :gloves:")
            packing_list.append('warm jacket')
            packing_list.append('gloves')
        if over_80:
            notes.append(f"Looks like its going to be hot!:sunglasses: Make sure to bring sunscreen and a hat")
            packing_list.append('shorts')
            packing_list.append('sunscreen')
            packing_list.append('hat')
        blocks = []
        blocks.append({
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Packing List for trip to {city.name}, {city.state}"
            }
        })
        for note in notes:
            blocks.append({"type": "section",
             "text": {"type": "mrkdwn",
                      "text": note}})
        list_str = ''
        for item in packing_list:
            list_str += f"- {item}\n"
        blocks.append(
            {"type": "section",
             "text": {"type": "mrkdwn",
                      "text": list_str}})
        blocks.append({"type": "divider"})
        say({"blocks": blocks})
    else:
        say(f"City:{city} not found")


@app.command("/weather")
def handle_weather_command(ack, body, say):
    # Acknowledge the command request
    ack()
    user_id = body["user_id"]
    if len(body["text"].split(" ")) != 2:
        say(f"<@{user_id}>, please enter a city and number of days")
        return
    city, days = body["text"].split(" ")
    if not days.isdigit() or int(days) < 1 or int(days) > 5:
        say(f"<@{user_id}>, please enter a valid number of days (1-5)")
        return
    city = weather.get_location(city)
    if city:
        forecast = weather.get_forecast(city.key)
        say_forecast(forecast, city, days, say)
    else:
        say(f"City:{city} not found")


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
