# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 11:27:15 2019

@author: d.padmanabhan.menon
"""
# Recursive Binary Search 

def binarySearch (arr, low, high, element): 

	if high >= low: 

		mid = int(low + (high - low)/2)

		if arr[mid] == element: 
			return mid 
		
		elif arr[mid] > element: 
			return binarySearch(arr, low, mid-1, element) 

		else: 
			return binarySearch(arr, mid + 1, high, element) 

	else: 
		return -1
    

arr = [ 2, 3, 4, 10, 40] 
element = 10
low = 0
high  = len(arr)-1

found = binarySearch(arr, low, high, element) 

if found != -1: 
	print("Element is present at index {}".format(found))
else: 
	print("Element is not present in array")
