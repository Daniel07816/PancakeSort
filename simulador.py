import random
import time

def flip(arr, i):
    start = 0
    while start < i:
        temp = arr[start]
        arr[start] = arr[i]
        arr[i] = temp
        start += 1
        i -= 1
 
def findMax(arr, n):
    mi = 0
    for i in range(0,n):
        if arr[i] > arr[mi]:
            mi = i
    return mi
 
def pancakeSort(arr, n):
     
    curr_size = n
    while curr_size > 1:
        mi = findMax(arr, curr_size)
 
        if mi != curr_size-1:
            flip(arr, mi)
            flip(arr, curr_size-1)
            printArray(arr, n)
            time.sleep(2)
        curr_size -= 1

def printArray(arr, n):
    print(arr)
    print("*************")
        


arr = []
for i in range (10):
    arr.append(random.randint(1,100))

n = len(arr)
pancakeSort(arr, n)
print ("Sorted Array ")
printArray(arr,n)