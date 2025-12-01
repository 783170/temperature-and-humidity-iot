#python

def quicksortFxn(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        beforePivot = [x for x in arr[1:] if x < pivot]
        afterPivot = [x for x in arr[1:] if x >= pivot]
        arr = quicksortFxn(beforePivot) + [pivot] + quicksortFxn(afterPivot)
    return arr