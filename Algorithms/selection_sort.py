from timing import timing
from test_data import unsorted_list

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

@timing
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


if __name__ == '__main__':

    print('{color}Selection sort algorithms example{endcolor}'.format(color='\033[1;33m', endcolor='\033[0m'))
    
    print(selectionSort([5, 6, 3, 7, 1, 4, 2, 8, 22, 35, 10, 99, 88, 95, 66, 25, 18, 98, 33, 37, 68, 55, 51, 59, 563, 999, 421, 684]))
    print('{color}Selection sort algorithms with 10 000 entries in list.{endcolor}\n'.format(color='\033[1;33m', endcolor='\033[0m'))
    selectionSort(unsorted_list)