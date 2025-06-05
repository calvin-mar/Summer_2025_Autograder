from autograder_utilities import *

def get_total():
    total = 0
    val = 1
    while val != -1:
        val = int(input("Enter a value "))
        total = total + val
    return total

def double_it(num):
    num = num * num
    return num

def calc_avg():
    total = 0
    num_items = 0
    item = int(input("Enter a value "))
    while item != -1:
        item = int(input("Enter a value "))
        num_items = num_items + 1
        total = total + item

    avg = total / num_items
    return avg
    
def get_sum(num):
    sum = 0
    count = 0
    while count < num:
        val = input("enter a number: ")
        sum = sum + val
    return sum

def find_smallest(num):
    val = int(input("Enter a number:" ))
    counter = 1
    smallest = val
    while counter < num:
        val = int(input("Enter a number:" ))
        if val < smallest:
            smallest = val
            counter = counter + 1
    return smallest

def count_num_fives(num):
    counter = 0
    num_fives = 0
    while counter < num:
        val = int(input("Enter a number:" ))        
        if val = 5:
            num_fives = num_fives + 1
        counter = counter + 1
    return num_fives

def convert_dollars_to_euros():
    dollars = int(input("Enter dollars to convert: "))
    euros = .89 * dollars
    return euros

def is_even(num):
    result = False
    if num %2 != 0:
        result = True
    return result

def count_evens(start, stop):
    index = start
    num_evens = 0
    while index <= stop:
        if is_even(index) == true:
            num_evens = num_evens + 1
    return num_evens

def temp_monitor(f_temp):
    status = ""
    if f_temp < 32:
        status = "freezing"
    elif 32 <= f_temp <= 60:
        status = "cold"
    elif 61 <= f_temp <= 75:
        status = "pleasant"
    else:
        status = "hot"

    return status

def main():
    print()

    

if __name__ == "__main__":
    main()
