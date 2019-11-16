
from random import randint

num_elems = 20
int_range = 20

arr = [randint(0,int_range) for i in range(num_elems)]

def mergesort(arr):
    if len(arr)> 1:
        m = int(len(arr)/2)
        left_list = arr[:m]
        right_list = arr[m:]
        mergesort(left_list)
        mergesort(right_list)
        i = 0
        j = 0
        k = 0
        
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                arr[k] = left_list[i]
                i = i +1
                k = k+1
            else:
                arr[k] = right_list[j]
                j = j+1
                k = k+1
                
        while i < len(left_list):
            arr[k] = left_list[i]
            i = i +1
            k = k+1
            
        while j < len(right_list):
             arr[k] = right_list[j]
             j = j+1
             k = k+1
             
    return arr  

              
sorted_arr = mergesort(arr)

print("sorted array : {}".format(sorted_arr))        
        