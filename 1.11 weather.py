###
# The weather station report
#
temperatures = [
    3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
    4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
    -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
]


def print_weather_report(temps):
    # number of mesaurements
    measurements = len(temps)

    # calculates average temperature
    temp_total = 0
    for temp in temperatures:
        temp_total += temp
    avg_temp = temp_total / measurements

    # calculates min and max temperatures
    min_temp = min(temps)
    max_temp = max(temps)

    # calculates number of days with negative temp
    negative_temp = 0
    i = 0
    while i < measurements:
        if temperatures[i] < 0:
            negative_temp += 1
        i += 1

    print(f"""TEMPERATURE REPORT 
Month: March
Number of measurements: {measurements}
Average temperature in the month: {avg_temp}
Minimum temperature: {min_temp}
Maximum temperature: {max_temp}
Number of days with negative temperature: {negative_temp}""")


# prints out month report
def main():
    print_weather_report(temps=temperatures)


if __name__ == '__main__':
    main()