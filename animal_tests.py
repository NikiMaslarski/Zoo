import unittest
from animal import Animal


class AnimalTests(unittest.TestCase):
    def setUp(self):
        self.test_animal = Animal("Tiger", 5, "Gencho", "male", 350, 10, "carnivore",
        50, 400, 25, (1, 50))

    def test_animal_grow(self):
        self.test_animal.grow(2)
        self.assertEqual(self.test_animal.weight, 400)
        self.assertEqual(self.test_animal.age, 7)

    def test_animal_consume(self):
        self.assertEqual(self.test_animal.consume(), 7)

    def test_animal_is_alive(self):
        self.assertTrue(self.test_animal.is_alive)
        for x in range(0, 10):
            self.test_animal.should_die()
        self.assertFalse(self.test_animal.is_alive)

if __name__ == '__main__':
    unittest.main()