from matplotlib import pyplot as plt
import csv
from datetime import datetime


def create_graph():
    data_dict = {}
    with open('data.txt', mode='r') as data_file:
        data_reader = csv.reader(data_file, delimiter=',')
        next(data_reader)
        count = 0
        for row in data_reader:
            if count < 96:
                data_dict.update({datetime.strptime(row[1],
                                                    '%Y-%m-%d %H:%M:%S.%f')
                                  : float(row[2])})
                count += 1
            else:
                break

    lists = (data_dict.items())
    x, y = zip(*lists)

    plt.plot(x, y, color='b')
    plt.xlabel('Time')
    plt.ylabel('Temperature')
    plt.savefig('temp_over_24_hrs.png')
