import csv


def transform():
    data_list = {}
    with open('data.txt', mode='r') as data_file:
        next(data_file)
        row_number = 1
        data_reader = csv.reader(data_file, delimiter=',')
        for row in data_reader:
            data_list.update({row_number: int(row[4])})
            row_number += 1

    with open('transform.txt', mode='w') as transform_file:
        transform_writer = csv.writer(transform_file, delimiter=',')
        transform_writer.writerow(['id', 'current_state', 'next_state'])
        for k, v in data_list.items():
            next_state = data_list.get(k + 1)
            if next_state is None:
                next_state = 0
            transform_writer.writerow([k, v, next_state])
