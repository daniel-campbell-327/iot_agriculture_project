import datetime
import csv
from sensor_data import sensor_data


def write_to_file() -> None:
    humidity_data, temperature_data = sensor_data()
    if temperature_data < 0:
        temp_state = 1
    elif 0 <= temperature_data  < 10:
        temp_state = 2
    elif 10 <= temperature_data < 20:
        temp_state = 3
    elif 20 <= temperature_data < 30:
        temp_state = 4
    else:
        temp_state = 5

    with open('data.txt', mode='r') as data_file:
        row_count = 0
        data_reader = csv.reader(data_file, delimiter=',')
        for row in data_reader:
            row_count += 1

    with open('data.txt', mode='a') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', )

        data_writer.writerow([row_count,
                              datetime.datetime.now(),
                              temperature_data,
                              humidity_data,
                             temp_state])
