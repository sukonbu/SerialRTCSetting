import serial
import serial.tools.list_ports
import time

#  serial test
ser = serial.Serial()
ser.baudrate = 9600
for i in range(100):
    try:
        ser.port = i
        ser.open()
        break
    except:
        i = i
while(true){
    ser.write("Hello")
    time.sleep(1.0)
}