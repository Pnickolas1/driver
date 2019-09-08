import unittest
from driver import Driver
from collections import OrderedDict

class TestDriver(unittest.TestCase):

    def test_sum_minutes_driven(self):
        """
        Test that will sum subtract endtime from starttime and sum that product
        """
        data = [['07:15', '07:45', '17.3'], ['06:12', '06:32', '21.8']]
        result = Driver.sum_minutes_driven(self, data)
        self.assertEqual(result, 50.0)

    def test_sum_miles_driven(self):
        """
        Test that will sum the length of each individual trip
        """
        data = [['07:15', '07:45', '17.3'], ['06:12', '06:32', '21.8']]
        result = Driver.sum_miles_driven(self, data)
        self.assertEqual(result, 39)

    def test_sort_dict_by_miles_driven(self):
        """
        Test that will take in a dict without any type of sorting,
        output is a dict sorted by miles (largest to smallest)
        """
        data = {'Dan': {'miles': 39, 'minutes': 50.0}, 'Alex': {'miles': 42, 'minutes': 75.0}, 'Bob': {'miles': 0, 'minutes': 0}}
        result = Driver._sort_by_miles(self, data)
        sortedByMiles = OrderedDict([('Alex', {'miles': 42, 'minutes': 75.0}), ('Dan', {'miles': 39, 'minutes': 50.0}), ('Bob', {'miles': 0, 'minutes': 0})])
        self.assertEqual(result, sortedByMiles)


if __name__ == "__main__":
    unittest.main()
