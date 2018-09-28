import context
import unittest
import pytest
from weather import Weather


class TestWeather(unittest.TestCase):
    def test_lookup_aggregate_condition_sunny(self):
        weather = Weather()

        condition = weather.lookup_aggregate_condition('32')
        self.assertTrue(condition == Weather.AggregateWeatherConditions.Sunny)

    def test_lookup_aggregate_condition_rainy(self):
        weather = Weather()

        condition = weather.lookup_aggregate_condition('15')
        self.assertTrue(condition == Weather.AggregateWeatherConditions.Raining)

    def test_lookup_aggregate_condition_cloudy(self):
        weather = Weather()

        condition = weather.lookup_aggregate_condition('27')
        self.assertTrue(condition == Weather.AggregateWeatherConditions.Cloudy)

    def test_lookup_aggregate_condition_unknown(self):
        weather = Weather()

        condition = weather.lookup_aggregate_condition('99')
        self.assertTrue(condition == Weather.AggregateWeatherConditions.Other)
