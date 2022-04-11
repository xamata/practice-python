# Change the input of an array so that the array begins with the even numbers first

def even_odd(arr):
	next_even, next_odd = 0, len(arr)-1
	while next_even < next_odd:
		if arr[next_even] % 2 == 0:
			next_even += 1
		else: 
			arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
			next_odd -=1

def main():
	arr = [1,5,7,3,2,6,3,3,4,8]
	even_odd(arr)
	print(arr)


if __name__ == "__main__":
	main()
