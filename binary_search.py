# status: still debugging
def binary_search(x, search_list):
    iterations = 1
    left = 0
    right = len(search_list)-1
    mid = (right + left)//2

    while search_list[mid] != x:
        if search_list[mid] <x:
            left = mid + 1
        else:
            right = mid - 1
        mid = (right + left)//2
        iterations += 1
    print('iterations = ', str(iterations))
    return mid

# will run into an error. still debugging.
print(binary_search(32, [4,8,9,10,24,45,50,56,32]))
