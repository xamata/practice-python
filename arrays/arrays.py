# arrays.py - Write out the methods for an array

import numpy as np

def arr_test(arr):
	print(arr)

	# adds last value to array
	arr.append(8)
	print(arr)

	# removes last value of array
	arr.pop()
	print(arr)

	print("index at four is "+ str(arr.index(3)))

	# reverses array
	arr.reverse()
	print(arr)

	# sort puts array in order
	arr.sort()
	print(arr)

	# arrays size using numpy
	print(np.size(arr, 0))

	# len of array
	print(len(arr))

def main():
	arr = [1,5,3,6,2,7]
	arr_test(arr)

if __name__ == "__main__":
	main()