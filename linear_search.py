
def linear_search(x, search_list):
    """
    returns the index of the target x, if found in the 
    list search_list or return -1 instead
    """
    iterations = 0
    
    while iterations < len(search_list):
        if x == search_list[iterations]:
            return iterations
        iterations += 1
    return -1

print(linear_search(20, [5,7,3,2,20,50,105,40]))
