class Zoo:

    def __init__(self, animals, capacity, buget):
        self.animals = animals
        self.capacity = capacity
        self.buget = buget

    def accommodate(self, animal):
        if len(self.animals) < self.capacity:
            self.animals.append(animal)
        else:
            raise OverflowError("No space for more animals")

    def get_daily_income(self):
        return len(self.animals) * 60

    def get_daily_outcome(self):
        total_daily_outcome = 0
        for animal in self.animals:
            if animal.food_type == "carnivore":
                total_daily_outcome += animal.consume() * 4
            elif animal.food_type == "herbivore":
                total_daily_outcome += animal.consume() * 2
        return total_daily_outcome

    def clear_death(self, dead_animal):
        self.animals = [animal for animal in
                        self.animals if animal.is_alive]

