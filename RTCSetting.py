import serial
import serial.tools.list_ports
import time

ser = serial.Serial()


def main():
    #  serial test
    ser.baudrate = 9600
    print('portCheck')
    ser.port = list(serial.tools.list_ports.comports())[0][0]
    print(ser.port)
    ser.open()
    read_serial()
    print('end setting')


def read_serial():
    while True:
        if ser.inWaiting() > 0:
            data = ser.readline()
            if 'uv' in data:
                print('connected device')
                ser.write('unko')
                break
    # serial message to Device (RTCmodule)


if __name__ == '__main__':
    main()
