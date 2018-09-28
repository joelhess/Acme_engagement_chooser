import context
import main
import unittest
from weather import Weather


class TestMain(unittest.TestCase):
    def test_map_conditions_to_contact_method_should_return_text(self):
        conditions = {'high': '80', 'condition_name': Weather.AggregateWeatherConditions.Sunny}
        contact_method = main.map_conditions_to_contact_method(conditions)
        self.assertIs(contact_method, main.ContactType.Text)

    def test_map_conditions_to_contact_method_warm_and_other_should_return_email(self):
        conditions = {'high': '80', 'condition_name': Weather.AggregateWeatherConditions.Other}
        contact_method = main.map_conditions_to_contact_method(conditions)
        self.assertIs(contact_method, main.ContactType.Email)

    def test_map_conditions_to_contact_method_should_return_email(self):
        conditions = {'high': '55', 'condition_name': Weather.AggregateWeatherConditions.Sunny}
        contact_method = main.map_conditions_to_contact_method(conditions)
        self.assertIs(contact_method, main.ContactType.Email)

    def test_map_conditions_to_contact_method_should_return_phone(self):
        conditions = {'high': '43', 'condition_name': Weather.AggregateWeatherConditions.Sunny}
        contact_method = main.map_conditions_to_contact_method(conditions)
        self.assertIs(contact_method, main.ContactType.Phone)

    def test_map_conditions_to_contact_method_should_return_phone_when_raining(self):
        conditions = {'high': '80', 'condition_name': Weather.AggregateWeatherConditions.Raining}
        contact_method = main.map_conditions_to_contact_method(conditions)
        self.assertIs(contact_method, main.ContactType.Phone)

    def test_format_condition_printout_invalid_params(self):
        with self.assertRaises(Exception) as cm:
            main.format_condition_printout("my string")

        self.assertEqual(cm.exception.args[0], 'Conditions must be a dictionary')
