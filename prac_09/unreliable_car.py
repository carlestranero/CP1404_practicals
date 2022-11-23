"""
CP1404 Practical - Carl Estranero - Unreliable Car
"""

from random import randint
from prac_09.car import Car

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability


    def drive(self,distance):
        trustworthiness = randint(0,100)
        if trustworthiness >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
