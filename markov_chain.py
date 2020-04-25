import csv
from analysis import get_next_state as gns


def markov_chain():
    with open('transform.txt', mode='r') as data_file:
        data_reader = csv.reader(data_file, delimiter=',')
        data_from_transform = [row for row in data_reader]
    given_state = data_from_transform[-1][1]

    for i in range(0, 4):
        given_state = gns(int(given_state))
    return given_state
