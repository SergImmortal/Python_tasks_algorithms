from timing import timing
from test_data import unsorted_list
from quick_sort import quickSort as sort
import math

@timing
def binaryBearch(target_list, item):
    low = 0
    high = len(target_list)-1

    while low <= high:
        mid = math.ceil((low+high)/2)
        guess = target_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = mid+1
    return None

sorted_list = sort(unsorted_list)

@timing
def bruteForce(target_list, item):
    for i in range(len(target_list)):
        if target_list[i] == item:
            return i

if __name__ == '__main__':
    print('{color}Binary search algorithms example.{endcolor}'.format(color='\033[1;33m', endcolor='\033[0m'))
    print('{color}\nSearch in list with 10 0000 entries used binary search:{endcolor}\n'
        .format(color='\033[1;33m', endcolor='\033[0m'))
    print(binaryBearch(sorted_list, 9527029))
    print('{color}\nSearch in list with 10 0000 entries used brute force method:{endcolor}\n'
        .format(color='\033[1;33m', endcolor='\033[0m'))
    print(bruteForce(sorted_list, 9527029))