
def fizz_buzz():
	fizz = 'Fizz'
	buzz = 'Buzz'
	fizz_buzz = 'FizzBuzz'

	for num in range(15):
		num +=1
		print(num)

		if num%3 ==0 and num%5 ==0:
		    print('output: {}'.format(fizz_buzz))

		elif num%3 == 0:
			print('output: {}'.format(fizz))

		elif num%5 ==0:
			print('output: ', buzz)

fizz_buzz()
	