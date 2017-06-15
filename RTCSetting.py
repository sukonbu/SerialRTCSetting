import serial
import serial.tools.list_ports
import time
from datetime import datetime

ser = serial.Serial()


def main():
    #  serial test
    ser.baudrate = 9600
    print('portCheck')
    ser.port = list(serial.tools.list_ports.comports())[0][0]
    print(ser.port)
    ser.open()
    read_serial()
    print('application end')


def read_serial():
    while True:
        if ser.inWaiting() > 0:
            data = ser.readline()
            if 'uv' in data:
                print('connected device')
                dt = datetime.now().strftime("%Y,%m,%d,%H,%M,%S")
                print(dt)
                ser.write(dt)
                break
    while True:
        if ser.inWaiting() > 0:
            data = ser.readline()
            if 'end' in data:
                print('setting complete!')
                break


if __name__ == '__main__':
    main()
