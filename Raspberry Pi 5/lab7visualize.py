
def averageFxn (data):
    #takes in the 2D array of all the data and the column that is being averaged
    sum = 0
    for i in range(len(data)):
        sum+=data[i]
    return round(sum/len(data),3)

def minFxn (data):
    #takes in the 2D array of all data and the column where the min value is being found
    min = 1000
    for i in range(len(data)):
        if data[i] < min:
            min = data[i]
    return min

def maxFxn (data):
    #takes in the 2D array of all data and the column where the min value is be>
    max = -1
    for i in range(len(data)):
        if data[i] > max:
            max = data[i]
    return max
