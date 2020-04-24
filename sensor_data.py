import serial
import time


def sensor_data():
    ser = serial.Serial('/dev/cu.usbmodem1424201', 9600, timeout=1)
    count = 0
    time.sleep(2)
    run_count = 0
    while run_count < 2:
        if count == 0:
            ser.flushInput()
            ser_bytes = ser.readline()
            count += 1
            time.sleep(10)
            run_count += 1
        elif count > 0:
            ser.flushInput()
            ser_bytes = ser.readline()
            humidity_data = int(ser_bytes[19:21])
            temperature_data = int(ser_bytes[41:43])
            time.sleep(10)
            run_count += 1
            return humidity_data, temperature_data
