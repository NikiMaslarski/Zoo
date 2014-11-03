import random


class Animal:

    def __init__(self, species, age, name, gender, weight,
        life_expectancy, food_type, newborn_weight, average_weight,
        weight_age_ratio, food_weight_ratio, gestation_period=None):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight
        self.life_expectancy = life_expectancy
        self.food_type = food_type
        self.newborn_weight = newborn_weight
        self.average_weight = average_weight
        self.weight_age_ratio = weight_age_ratio
        self.food_weight_ratio = food_weight_ratio
        if gender == "female":
            self.gestation_period = gestation_period
        self.is_alive = True

    def grow(self, age):
        expected_weight_grow = self.weight_age_ratio * age
        if self.weight + expected_weight_grow <= self.average_weight:
            self.weight += expected_weight_grow
            self.age += age

    def consume(self):
        return self.weight // (self.food_weight_ratio[1] / self.food_weight_ratio[0])

    def should_die(self):
        if random.random() > self.age / self.life_expectancy:
            self.is_alive = False