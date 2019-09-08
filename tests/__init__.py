import unittest
from driver import Driver

class TestDriver(unittest.TestCase):

    def test_sum_minutes_driven(self):
        self.assertEqual(Driver.sum_minutes_driven(self, [['07:15', '07:45', '17.3'], ['06:12', '06:32', '21.8']]
), 50.0)
        self.assertEqual(Driver.sum_minutes_driven(self, [['12:01', '13:16', '42.0']]
), 75.0)

    def test_sum_miles_driven(self):
        self.assertEqual(Driver.sum_miles_driven(self, [['07:15', '07:45', '17.3'], ['06:12', '06:32', '21.8']]
), 39)
        self.assertEqual(Driver.sum_miles_driven(self, [['12:01', '13:16', '42.0']]
), 42)


if __name__ == "__main__":
    unittest.main()