import unittest

from zoo import Zoo


class TestZoo(unittest.TestCase):

    def setUp(self):
        self.zoo = Zoo([], 10, 5000)

    def test_constructor(self):
        self.assertEqual(self.zoo.capacity, 10)
        self.assertEqual(self.zoo.buget, 5000)


if __name__ == "__main__":
    unittest.main()
