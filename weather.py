import urllib.request
import urllib.parse
import json
from enum import Enum


class Weather(object):
    def __init__(self, woeid = None):
        self.location = woeid or 2452078 # This is the Id for Minneapolis
        self.base_url = "https://query.yahooapis.com/v1/public/yql?"
        # these map the codes from yahoo's condition types to their root type
        self.condition_map = {
            "sunny": [32],
            "raining": [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17],
            "cloudy": [27,28,29,30],
            "other": []
        }

    # Get and format the results from the api.
    def get_weather_conditions(self):
        weather_result = self.get_weather_conditions_from_api(self.location)

        data = {}
        for day in weather_result['query']['results']['channel']:
            data[day['item']['forecast']['date']] = \
                {
                    'high': day['item']['forecast']['high'],
                    'condition_code': day['item']['forecast']['code'],
                    'condition_name': self.lookup_aggregate_condition(day['item']['forecast']['code'])
                }

        return data

    def get_weather_conditions_from_api(self, location):
        yql_query = f"select item.forecast from weather.forecast where woeid={location}"
        yql_url = self.base_url + urllib.parse.urlencode({'q': yql_query}) + "&format=json"
        request = urllib.request.Request(yql_url)
        result = urllib.request.urlopen(request).read()
        data = json.loads(result)

        return data

    # Map the condition from the api to an aggregate type.
    def lookup_aggregate_condition(self, condition_code):
        # if for some reason, we get something weird back for hte code, return UNKNOWN.
        try:
            code = int(condition_code)
        except ValueError:
            print("Unrecognized Code")
            return self.AggregateWeatherConditions.UNKNOWN

        if code in self.condition_map["sunny"]:
            return self.AggregateWeatherConditions.Sunny
        elif code in self.condition_map["raining"]:
            return self.AggregateWeatherConditions.Raining
        elif code in self.condition_map["cloudy"]:
            return self.AggregateWeatherConditions.Cloudy

        return self.AggregateWeatherConditions.Other

    class AggregateWeatherConditions(Enum):
        UNKNOWN = -1
        Sunny = 0
        Raining = 1
        Cloudy = 2
        Other = 99

        def __str__(self):
            return self.name


