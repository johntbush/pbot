import requests
from datetime import datetime
class City:
    def __init__(self, key, name, state, country, latitude, longitude):
        self.key = key
        self.name = name
        self.state = state
        self.country = country
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        return f"{self.name}, {self.state} {self.country}"

    def __repr__(self):
        return f"{self.name}, {self.state} {self.country}"

class DailyForecast:
    def __init__(self, date, min_temp, max_temp, day, night, precipitation, link):
        self.date_short = datetime.fromisoformat(date).strftime("%m/%d")
        self.date = datetime.fromisoformat(date)
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.day = day
        self.night = night
        self.link = link
        self.precipitation = precipitation

    def __str__(self):
        return f"{self.date_short} - Min: {self.min_temp}F, Max: {self.max_temp}F, Day: {self.day}, Night: {self.night}"

    def __repr__(self):
        return f"{self.date_short} - Min: {self.min_temp}F, Max: {self.max_temp}F, Day: {self.day}, Night: {self.night}"


class Weather:
    def __init__(self, key):
        self.key = key

    def get_location(self, q):
        url = f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey={self.key}&q={q}"
        data = requests.get(url).json()
        #print(data)
        if len(data) > 0:
            lat = data[0].get('GeoPosition',{}).get('Latitude')
            lon = data[0].get('GeoPosition',{}).get('Longitude')
            key = data[0].get('Key')
            name = data[0].get('LocalizedName')
            state = data[0].get('AdministrativeArea',{}).get('LocalizedName')
            country = data[0].get('Country',{}).get('LocalizedName')
            return City(key, name, state, country, lat, lon)
        return None

    def get_forecast(self, location):
        url =f"http://dataservice.accuweather.com/forecasts/v1/daily/5day/{location}?apikey={self.key}"
        data = requests.get(url).json()
        print(data)
        response = []
        for day in data['DailyForecasts']:
            precipitation = True if day['Day']['HasPrecipitation'] or day['Night']['HasPrecipitation'] else False
            day_precipitation = 'with precipitation' if day['Day']['HasPrecipitation'] else 'without precipitation'
            night_precipitation = 'with precipitation' if day['Night']['HasPrecipitation'] else 'without precipitation'
            forecast = DailyForecast(
                date=day['Date'],
                min_temp=day['Temperature']['Minimum']['Value'],
                max_temp=day['Temperature']['Maximum']['Value'],
                day=day['Day']['IconPhrase'] + ' ' + day_precipitation,
                night=day['Night']['IconPhrase'] + ' ' + night_precipitation,
                precipitation=precipitation,
                link=day['Link']
            )
            response.append(forecast)
        return response
