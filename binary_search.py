# status: still needs debugging
def binary_search(item, search_list):
    """
    implements a binary search with an item
    and an item list.
    returns the position of the item if found in the list
    """
    iterations = 1
    far_left = 0
    far_right = len(search_list)-1
    mid_position = (far_right + far_left)//2

    while item != search_list[mid_position]:

        if item < search_list[mid_position]:
            far_left = 0
            far_right = mid_position
            for i in range(far_left, far_right):
                if item == search_list[i]:
                    return i
                    break
                i = i+1
        elif item > search_list[mid_position]:
            far_left = + 1
            far_right = len(search_list)

            for i in range(far_left, far_right):
                if item == search_list[i]:
                    return i
                    break
                i + i+1

        iterations += 1

    print('number of searches = ', str(iterations))
    return mid_position


item = 10
search_list = [4,8,9,10,24,45,30,50,32,56]
sorted_search_list = sorted(search_list)

print(sorted_search_list)
print(binary_search(item, sorted_search_list))
