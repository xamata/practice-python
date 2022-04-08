def selectionSort(array, size):
	# size is len(array)
	for step in range(size):
		min_idx = step

		for i in range(step+1, size):
			if array[i] < array[min_idx]:
				min_idx = i


		# put min in correct position
		(array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 4, 45, 0, 11, -9]
size = len(data)
print(data)
selectionSort(data, size)
print(data)
