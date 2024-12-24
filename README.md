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

# Task #1: Implement the `handle_weather_command` function

Validation:
- make sure sends in two inputs the city name and the number of days
- make sure the number of days is a valid integer
- if the validation fails let the user know what the problem is

Make a call to the weather service with the city name:

`   city = weather.get_location(city_name)`

If the city is valid get the forecast and say it to the user:

```
    forecast = weather.get_forecast(city.key)
    say_forecast(forecast, city, days, say)
```

If the city is not valid let the user know

# Task #2: Implement the `handle_pack_command` function

Validation:
- make sure sends in two inputs the city name and the number of days
- make sure the number of days is a valid integer
- if the validation fails let the user know what the problem is

If the city is valid get the forecast, and return back a packing list.
The packing list should include standard things a scout would need on 
any trip and then based on the temperature additional items.

If its under 30 what would you need ?
If its under 60 what would you need ?
If its over 80 what would you need ?

How would you figure out the coldest or hotest it's going to be ?

Bonus points for being specific about how many clothes items to bring based
on the number of days of the trip.