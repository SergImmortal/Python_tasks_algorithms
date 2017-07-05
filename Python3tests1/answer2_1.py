# -*- coding: utf-8 -*-
import re


# Decorator for improve appearance of results of sort
def output_with_prefix(func):
    def wrapped(arg):
        target = func(arg)
        print('\n==========results==========')
        for elem in target:
            if elem[2] == "М":
                print(" Г-н  ", elem[0], elem[1])
            elif elem[2] == "Ж":
                print(" Г-жа ", elem[0], elem[1])

    return wrapped


# Function which sort input value by age
# Parameters: first - list with request,  second - list with string
# Return: print results of counting
@output_with_prefix
def sorting_list_by_name(datalist):
    datalist.sort(key=lambda i: i[3])
    return datalist


# Function for opening file with data
# Parameter: first - path to the file
# Return: list with data
def open_file(waytofile):
    with open(waytofile, "r", encoding="utf8") as data:
        amount = int(data.readline().strip())
        datalist = []
        for line in range(amount):
            datalist.append(data.readline().strip().split())
    return datalist


# Description for input data
value = input('Dear user, please input path to file with data or '
    'quantity elements for creating array and then entered data. '
    '(In one string, values have to separated by a space) \n'
    )
# If path to file look like for Linux ow Windows file system
if re.match(r'^\/', value) or re.match(r'^([a-zA-Z]:)?\\', value):
    datalist = open_file(value)
    sorting_list_by_name(datalist)
# If data is going to input with keyboard
else:
    quantityOfIteration = int(value[0])
    datalist = []
    for list_i in range(quantityOfIteration):
        list_temp = input().strip().split(' ')
        datalist.append(list_temp)
    sorting_list_by_name(datalist)
