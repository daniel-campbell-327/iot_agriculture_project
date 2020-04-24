import csv
import smtplib
import ssl
from markov_chain import markov_chain as mc
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(contain_graph):
    with open('data.txt', mode='r') as data_file:
        data_reader = csv.reader(data_file, delimiter=',')
        data_from_csv = [row for row in data_reader]

    temp = int(data_from_csv[-1][2])
    humidity = int(data_from_csv[-1][3])
    if mc() == 1:
        plant_state = 'extremely cold'
    elif mc() == 2:
        plant_state = 'cold'
    elif mc() == 3:
        plant_state = 'okay'
    elif mc() == 4:
        plant_state = 'hot'
    elif mc() == 5:
        plant_state = 'extremely hot'
    acc_context = ssl.create_default_context()
    smtp_server = 'smtp.gmail.com'
    msg_from = 'danielcampbelltest@gmail.com'
    msg_subject = 'Plant Temperature Status'
    msg_body = (f'The current temperature of the plant is {temp}'
                        f' and the current humidity is {humidity}. '
                        f'In one hours time the plant will be {plant_state}.')
    msg_attach = 'temp_over_24_hrs.png'

    message = MIMEMultipart()
    message['From'] = msg_from
    message['To'] = msg_from
    message['Subject'] = msg_subject

    message.attach(MIMEText(msg_body, 'plain'))

    if contain_graph:
        with open(msg_attach, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())

        encoders.encode_base64(part)

        part.add_header('Content-Disposition',
                        f'attachment; filename= {msg_attach}',)

        message.attach(part)

    text = message.as_string()

    with smtplib.SMTP_SSL(smtp_server, context=acc_context) as server:
        server.login(msg_from, 'testtest1!')
        server.sendmail(msg_from, msg_from, text)
