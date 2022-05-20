from array import *

arr =[44,30,24,32,35,30,40,38,15]
size = len(arr)
def maxDiff(arr, arr_size):

    max_diff = arr[1] - arr[0]
     
    for i in range( arr_size ):
        for j in range( i+1, arr_size ):
            if(arr[j] - arr[i] > max_diff):
                max_diff = arr[j] - arr[i]
     
    return max_diff
print ("Maximum difference is", maxDiff(arr, size))
    