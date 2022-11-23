"""
CP1404 Practical - Carl Estranero - Silver Service Taxi
"""

from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def __str__(self):
        return f"{super().__str__()} in addition of the flagfall ${self.flagfall}"

    def get_fare(self):
        return super().get_fare() + self.flagfall