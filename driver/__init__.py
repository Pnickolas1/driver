import sys
from datetime import datetime, timedelta
from collections import OrderedDict


class Driver:

    def __init__(self, data):
        self.data = data

    def calculate_miles_driven(self, data):
        miles = 0
        for trip in data:
            miles += float(trip[2])
        total_miles = round(miles)
        return total_miles

    def calculate_minutes_driving(self, data):
        minutes = 0
        for d in data:
            start = datetime.strptime(d[0], '%H:%M')
            end = datetime.strptime(d[1], '%H:%M')
            time_difference = end - start
            time_difference_in_minutes = time_difference / timedelta(minutes=1)
            minutes += time_difference_in_minutes
        return minutes

    def _perform_diagnostics(self, drivers, telemetry):
        driver_meta_data = {}
        for driver in drivers:
            if driver not in telemetry:
                driver_meta_data[driver] = {'miles': 0, 'minutes': 0}
            else:
                miles = self.calculate_miles_driven(telemetry[driver])
                minutes = self.calculate_minutes_driving(telemetry[driver])
                driver_meta_data[driver] = {f"miles": miles, "minutes": minutes}
        return self._sort_by_miles(driver_meta_data)

    def _sort_by_miles(self, stats):
        return OrderedDict(sorted(stats.items(), key=lambda i: i[1]['miles'], reverse=True))


    def driving_summary(self):
        data = self.data
        drivers = []
        telemetry_data = {}
        for line in data:
            split_out = line.split(' ')
            if split_out[0] == 'Driver':
                drivers.append(split_out[1])
            else:
                if split_out[1] not in telemetry_data:
                    telemetry_data[split_out[1]] = [split_out[2:]]
                else:
                    telemetry_data[split_out[1]].append(split_out[2:])
        return self._perform_diagnostics(drivers, telemetry_data)
