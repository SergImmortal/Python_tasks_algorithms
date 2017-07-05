# -*- coding: utf-8 -*-
import re


# Decorator for improve appearance of result
def improvement_display_results(func):
    def wrapper(arg1, arg2):
        print('\n==========results=========')
        func(arg1, arg2)
    return wrapper


# Function for count amount of request in list
# Parameters: first - list with request,  second - list with string
# Return: print results of counting
@improvement_display_results
def counter_for_request(request_list, string_list):
    for list_elem in request_list:
        i = list_elem
        output = string_list.count(i)
        print('', list_elem, '-', output)


# Function for opening file with data
# Parameter: first - path to the file
# Return: list with request and list with string
def open_file(waytofile):
    string_list = []
    request_list = []
    with open(waytofile, "r", encoding="utf8") as data:
# Create list with string
        amt_string = int(data.readline().strip())
        for string in range(amt_string):
            string_list.append(data.readline().strip())
# Create list with request
        amt_request = int(data.readline().strip())
        for request in range(amt_request):
            request_list.append(data.readline().strip())
    return request_list, string_list


string_value = input('Dear user, please input path to file with data or data for creating lists. \n')
# If path to file look like for Linux file system
if re.match(r'^\/', string_value) or re.match(r'^([a-zA-Z]:)?\\', string_value):
    request_list, string_list = open_file(string_value)
    counter_for_request(request_list, string_list)
# If data is going to input with keyboard
else:
    quantityOfIteration = int(string_value)
    string_list = []
    for list_i in range(quantityOfIteration):
        list_temp = input().strip()
        string_list.append(list_temp)
    request_value = input()
    quantityOfIteration = int(request_value)
    request_list = []
    for list_i in range(quantityOfIteration):
        list_temp = input().strip()
        request_list.append(list_temp)
    counter_for_request(request_list, string_list)

