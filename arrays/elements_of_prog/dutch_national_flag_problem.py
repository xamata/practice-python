# dutch_national_flag_problem.py - select a pivot and reorders the array based on if it's less than/equal to or greater than

def dutch_flag_partition(pivot_index,A):
	pivot = A[pivot_index]
	# First pass: group elements smaller than pivot
	for i in range(len(A)):
		# Look for a smaller element
		for j in range(i+1, len(A)):
			if A[j] < pivot: 
				A[i], A[j] = A[j], A[i]
				break