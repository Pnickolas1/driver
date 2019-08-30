import sys
from datetime import datetime, timedelta
from driver import Driver


def calculate_miles_driven(driver, data):
    miles = 0
    for trip in data:
        miles += float(trip[2])
    total_miles = round(miles)
    return total_miles

def calculate_minutes_driving(driver, data):
    minutes = 0
    for d in data:
        start = datetime.strptime(d[0], '%H:%M')
        end = datetime.strptime(d[1], '%H:%M')
        time_difference = end - start
        time_difference_in_minutes = time_difference / timedelta(minutes=1)
        minutes += time_difference_in_minutes
    return minutes


def perform_diagnostics(drivers, telemetry):
    cumulative_miles = []
    driver_meta_data = {}
    for driver in drivers:
        if driver not in telemetry:
            driver_meta_data[driver] = {'miles': 0, 'minutes': 0}
        else:
            miles = calculate_miles_driven(driver, telemetry[driver])
            minutes = calculate_minutes_driving(driver, telemetry[driver])
            driver_meta_data[driver] = {f"miles": miles, "minutes": minutes}
    return driver_meta_data


def get_driver_data(data):
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
    return perform_diagnostics(drivers, telemetry_data)


def main():
    with open(sys.argv[1], "r") as f:
        contents = f.read().split('\n')
    print(get_driver_data(contents))

if __name__ == "__main__":
    main()