from writing_to_csv import write_to_file
from send_email import send_email
from time import sleep
from transform_txt import transform
from graphing_solutions import create_graph

run_count = 0
while True:
    write_to_file()
    run_count += 1
    # if the count is == to 96 send both the graph and analysis
    if run_count == 96:
        transform()
        create_graph()
        send_email(True)
        run_count = 0
    # if the count is divisible by 4 just do the predictive analysis
    elif run_count % 4 == 0:
        transform()
        send_email(False)
    sleep(900)



