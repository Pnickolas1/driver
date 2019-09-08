from datetime import datetime, timedelta
from collections import OrderedDict


class Driver:

    def __init__(self, data):
        self.data = data

    def sum_miles_driven(self, data):
        miles = 0
        for trip in data:
            miles += float(trip[2])
        total_miles = round(miles)
        return total_miles

    def sum_minutes_driven(self, data):
        minutes = 0
        for d in data:
            start = datetime.strptime(d[0], '%H:%M')
            end = datetime.strptime(d[1], '%H:%M')
            time_difference = end - start
            time_difference_in_minutes = time_difference / timedelta(minutes=1)
            minutes += time_difference_in_minutes
        return minutes

    def _perform_diagnostics(self, drivers, telemetry):
        print(telemetry)
        driver_meta_data = {}
        for driver in drivers:
            if driver not in telemetry:
                driver_meta_data[driver] = {'miles': 0, 'minutes': 0}
            else:
                miles = self.sum_miles_driven(telemetry[driver])
                minutes = self.sum_minutes_driven(telemetry[driver])
                driver_meta_data[driver] = {f"miles": miles, "minutes": minutes}
        print(driver_meta_data)
        return self._sort_by_miles(driver_meta_data)

    def _sort_by_miles(self, stats):
        return OrderedDict(sorted(stats.items(), key=lambda i: i[1]['miles'], reverse=True))

    def __print_output(self, data):
        for d in data:
            name = d
            miles = data[d]['miles']
            minutes = data[d]['minutes']
            if miles > 0:
                speed = round((miles / minutes * 60))
                print(f"{name}: {miles} miles @ {speed} mph")
            else:
                print(f"{name}: {miles} miles")

    def driving_summary(self):
        data = self.data
        drivers = []
        telemetry_data = {}
        for line in data:
            split = line.split(' ')
            if split[0] == 'Driver':
                drivers.append(split[1])
            else:
                if split[1] not in telemetry_data:
                    telemetry_data[split[1]] = [split[2:]]
                else:
                    telemetry_data[split[1]].append(split[2:])
        orgdata = self._perform_diagnostics(drivers, telemetry_data)
        self.__print_output(orgdata)

