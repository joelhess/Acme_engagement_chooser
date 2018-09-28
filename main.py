from weather import Weather
from enum import Enum, auto


def getConditions():
    weather = Weather()
    conditions = weather.get_weather_conditions()

    return conditions


def format_condition_printout(conditions):
    if not isinstance(conditions, dict):
        raise Exception('Conditions must be a dictionary')

    for day, values in conditions.items():
        print(f"The conditions for {day} are: ")
        print(f"  High:         {values['high']}")
        print(f"  Condition:    {str(values['condition_name'])}")
        print("")
        print(f"  The Optimal Outreach Method is:   {str(map_conditions_to_contact_method(values))}")
        print("")


def map_conditions_to_contact_method(condition_values):
    condition_temp = int(condition_values['high'])
    condition_name = condition_values['condition_name']

    contact_method = ContactType.Unknown

    if condition_temp > 75 and condition_name == Weather.AggregateWeatherConditions.Sunny:
        contact_method = ContactType.Text
    elif 55 <= condition_temp <= 75:
        contact_method = ContactType.Email
    elif condition_temp < 55:
        contact_method = ContactType.Phone
    else:
        contact_method = ContactType.Email

    if condition_name == Weather.AggregateWeatherConditions.Raining:
        contact_method = ContactType.Phone

    return contact_method


class ContactType(Enum):
    Unknown = auto()
    Text = auto()
    Email = auto()
    Phone = auto()

    def __str__(self):
        return self.name


if __name__ == '__main__':

    print('------------------------------------------------------')
    print('-- Thank you for requesting the best contact method --')
    print('------------------------------------------------------')

    conditions = getConditions()
    format_condition_printout(conditions)


