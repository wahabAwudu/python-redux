# the following functions takes a list and get two numbers whose sum is the target

def function_1(nums, target):
	for i in nums:
		for j in nums:
			if i+j == target: print(nums.index(i), nums.index(j))

numbers = [2,3,5,6,7,1,8]
target = 8
# function_1(numbers, target)

def function_2(nums, target):
	for num in nums:
		if num < target:
			diff = target - num
			if diff in nums:
				print('first: {} and second: {}'.format(num, diff))

function_2(numbers, target)