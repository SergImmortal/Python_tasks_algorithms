from timing import timing
from random import randrange
import random
from test_data import unsorted_list

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        index = randrange(len(arr))
        fulcrum = arr[index]
        less = [i for i in arr[:index] + arr[index+1:] if i <= fulcrum]
        greater = [i for i in arr[:index] + arr[index+1:] if i > fulcrum]
    return quickSort(less) + [fulcrum] + quickSort(greater)

@timing
def sort(x):
    return quickSort(x)

if __name__ == '__main__':
    print('{color}Quick sort algorithms example.{endcolor}\n'.format(color='\033[1;33m', endcolor='\033[0m'))

    print(sort([5, 6, 3, 7, 1, 4, 2, 8, 22, 35, 10, 99, 88, 95, 66, 25, 18, 98, 33, 37, 68, 55, 51, 59, 563,
                999, 421, 684, ]))
    print('{color}Quick sort algorithms with 10 000 entries in list.{endcolor}\n'.format(color='\033[1;33m', endcolor='\033[0m'))
    sort(unsorted_list)