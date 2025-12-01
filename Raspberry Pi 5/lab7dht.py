import time
import board
import adafruit_dht

sensor = adafruit_dht.DHT11(board.D4) 

def dhtRead ():
    try:
        tempC = sensor.temperature
        tempF = tempC * (9 / 5) + 32
        hum = sensor.humidity
        #print("Temp={0:0.1f}ºC, Temp={1:0.1f}ºF, Humidity={2:0.1f}%".format(temperature_c, temperature_f, humidity))
        return [round(tempF,2), round(tempC,2), round(hum,2)]

    except RuntimeError as error:
        print(error.args[0])
        time.sleep(1.0)
        return dhtFxn()
    except Exception as error:
        sensor.exit()
        print(error.args[0])
        return dhtFxn()
    #time.sleep(1.0)

def dhtExit ():
    sensor.exit()

