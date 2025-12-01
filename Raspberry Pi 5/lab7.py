import  lab7dht as dht
import lab7uart as uart
import lab7visualize as vis
import lab7email as email
import lab7quicksort as sort
import lab7API as API
import matplotlib.pyplot as plt
import csv

# additionally library
# gets current weather condictions for St. Paul
print("\n\n")
API.getweather("St. Paul")
print("\n")


filename = "lab7tempData.csv"
dataRows = [None]*21
dataRows[0] = ["MCP_F","MCP_C","DHT_F","DHT_C","DHT_HUM","%ERROR_F","%ERROR_C"]
dataCount = 0;

MCP_F = [None]*20
MCP_C = [None]*20
DHT_F = [None]*20
DHT_C = [None]*20
DHT_H = [None]*20
ERR_F = [None]*20
ERR_C = [None]*20


# reads 20 data points from DHT and MCP9700A sensors and prints them to terminal
print("MCP9700A\tDHT11\t\t\t%error")
print("tempF\ttempC\ttempF\ttempC\thum\ttempF\ttempC")

while dataCount < 20:
    uartData = uart.uartRead()
    dhtData = dht.dhtRead()    
    errorF = (dhtData[0]-uartData[0])/dhtData[0]*100
    errorF = round(abs(errorF),2)
    errorC = (dhtData[1]-uartData[1])/dhtData[1]*100
    errorC = round(abs(errorC),2)
    
    print(uartData[0],"\t",uartData[1],"\t",dhtData[0],"\t",dhtData[1],"\t",dhtData[2],"\t",errorF,"%\t",errorC,"%")
    dataRows[dataCount+1] = [uartData[0],uartData[1],dhtData[0],dhtData[1],dhtData[2],errorF,errorC]
    
    MCP_F[dataCount] = uartData[0]
    MCP_C[dataCount] = uartData[1]
    DHT_F[dataCount] = dhtData[0]
    DHT_C[dataCount] = dhtData[1]
    DHT_H[dataCount] = dhtData[2]
    ERR_F[dataCount] = errorF
    ERR_C[dataCount] = errorC
    
    #if the tempreture is above 20 degrees C send an email
    if (dhtData[1] > 0):
        email.sendEmail(dhtData[1])
    
    dataCount+=1
    
dht.dhtExit()
    

# writes the data to a csv file
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(dataRows)


# prints the average, min, and max for each value
print("\n\n\taverage\tmin\tmax")
print("MCP_F:\t",vis.averageFxn(MCP_F),"\t",vis.minFxn(MCP_F),"\t",vis.maxFxn(MCP_F))
print("MCP_C:\t",vis.averageFxn(MCP_C),"\t",vis.minFxn(MCP_C),"\t",vis.maxFxn(MCP_C))
print("DHT_F:\t",vis.averageFxn(DHT_F),"\t",vis.minFxn(DHT_F),"\t",vis.maxFxn(DHT_F))
print("DHT_C:\t",vis.averageFxn(DHT_C),"\t",vis.minFxn(DHT_C),"\t",vis.maxFxn(DHT_C))
print("DHT_H:\t",vis.averageFxn(DHT_H),"\t",vis.minFxn(DHT_H),"\t",vis.maxFxn(DHT_H))
print("ERR_F:\t",vis.averageFxn(ERR_F),"\t",vis.minFxn(ERR_F),"\t",vis.maxFxn(ERR_F))
print("ERR_C:\t",vis.averageFxn(ERR_C),"\t",vis.minFxn(ERR_C),"\t",vis.maxFxn(ERR_C),"\n\n")


# prints the sorted and unsorted DHT tempreture readings
print("UNSORTED:\t",DHT_C)
print("SORTED:\t",sort.quicksortFxn(DHT_C))


# plots the graphs for tempreture in C and in F for both sensors, the humidity, and the error
fig, axs = plt.subplots(2,2)
axs[0,0].plot(MCP_F)
axs[0,0].plot(DHT_F)
axs[0,0].set_title("Degrees F")

axs[0,1].plot(MCP_C)
axs[0,1].plot(DHT_C)
axs[0,1].set_title("Degrees C")

axs[1,0].plot(DHT_H)
axs[1,0].set_title("Humidity")

axs[1,1].plot(ERR_F)
axs[1,1].set_title("Error")

plt.tight_layout()
plt.show()
