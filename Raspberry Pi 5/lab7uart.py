import serial
from time import sleep

ser = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=3)

    
def uartRead ():
    data = 0
    tempC = 0
    tempF = 0
    data = ser.read(2)
    data = int.from_bytes(data, "little")
    tempC = ((data*3.3/4096.0)-0.5)*100.0
    tempF = (tempC*1.8)+32.0
    return [round(tempF,2), round(tempC,2)]
