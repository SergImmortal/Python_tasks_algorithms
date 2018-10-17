from test_data import unsorted_list
from quick_sort import sort as quickSort
from selection_sort import selectionSort

if __name__ == "__main__":
    print('{color}Sorting algorithms comparison.{endcolor}\n'.format(color='\033[1;33m', endcolor='\033[0m'))
    print('{color}Quick sort algorithms with 10 000 entries in list.{endcolor}\n'.format(color='\033[1;33m', endcolor='\033[0m'))
    quickSort(unsorted_list)
    print('{color}\nSelection sort algorithms with 10 000 entries in list.{endcolor}\n'.format(color='\033[1;33m', endcolor='\033[0m'))
    selectionSort(unsorted_list)