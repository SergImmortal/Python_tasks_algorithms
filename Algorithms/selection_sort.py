from timing import timing

print('{color}Selection sort algorithms example{endcolor}'.format(color='\033[42m', endcolor='\033[0m'))

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

print(selectionSort([5, 6, 3, 7, 1, 4, 2, 8]))