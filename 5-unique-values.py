
def unique_values():
    """
    accepts user input of 5 numbers.

    uses a python set to automatically remove duplicates from a list of 
    added numbers.

    prints 'Duplicate' when the length of the set is less than the length
    of digits expected (i.e 5, in our case) due to removed duplicates.
    
    prints 'All Unique' when the length of the set is equal to the expected length
    of digits (i.e. 5).
    """
    
    set_of_numbers = set()

    digits_limit = 5

    for i in range(digits_limit):
        iter_position = i+1
        num = input('Enter digit ' + str(iter_position) + ' :')
        set_of_numbers.add(num)

    if len(set_of_numbers) < 5:
	    print('Duplicates')
    elif len(set_of_numbers) == 5:
        print('All Unique')

unique_values()
