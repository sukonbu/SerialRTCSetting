import serial
import serial.tools.list_ports
import time

#  serial test
ser = serial.Serial()
ser.baudrate = 9600
print('portCheck')
for i in range(100):
    try:
        print('port found No.' + i)
        ser.port = i
        ser.open()
        read_serial()
        break
    except:
        i = i
print('end setting')


def read_serial():
    while True:
        if ser.inWaiting() > 0:
            data = ser.readline()
            if 'uv' in data:
                print('connected device')
                ser.write('s')
                break
    # serial message to Device (RTCmodule)
