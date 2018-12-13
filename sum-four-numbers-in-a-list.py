
def four_numbers(nums, target):
	quad = []

	for i in nums:
		for j in nums:
			for k in nums:
				for l in nums:
					if i+j+k+l == target: print('1st: {} 2nd: {} 3rd: {} 4th: {}' .format(i,j,k,l))

numbers = [2,3,5,6,7,1,8]
four_numbers(numbers, 8)
