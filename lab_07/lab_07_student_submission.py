# adds sentinel value of -1
if __name__ != "__main__":
    from autograder_assistant import input

def get_total():
    total = 0
    val = int(input("Enter a value "))
    while val != -1:
        total = total + val
        val = int(input("Enter a value "))
        
    return total

# squares instead of doubling
def double_it(num):
    num = num * 2 + 1
    return num

# loop broken
def calc_avg():
    total = 0
    num_items = 0
    item = int(input("Enter a value "))
    while item != -1:
        num_items = num_items + 1
        total = total + item
        item = int(input("Enter a value "))
    avg = total / num_items
    return avg
    
# infinite loop and cast not done
def get_sum(num):
    sum = 0
    count = 0
    while count < num:
        val = int(input("enter a number: "))
        sum = sum + val
        count = count + 1
    return sum

# counter only increased sometimes
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

# = instead of == for comparison
def count_num_fives(num):
    counter = 0
    num_fives = 0
    while counter < num:
        val = int(input("Enter a number:" ))        
        if val == 5:
            num_fives = num_fives + 1
        counter = counter + 1
    return num_fives

# cast not done right (should be float, not int)
def convert_dollars_to_euros():
    dollars = float(input("Enter dollars to convert: "))
    euros = .89 * dollars
    return euros

# logic backwards
def is_even(num):
    result = False
    if num %2 == 0:
        result = True
    return result

# infinite loop, range wrong, uses true instead of True    
def count_evens(start, stop):
    if start > stop:
        temp = stop
        stop = start
        start = temp
    index = start + 1
    num_evens = 0
    while index < stop:
        if is_even(index) == True:
            num_evens = num_evens + 1
        index = index + 1
    return num_evens

def temp_monitor(f_temp):
    status = ""
    if f_temp < 32:
        status = "freezing"
    elif 32 <= f_temp <= 60:
        status = "cold"
    elif 60 < f_temp <= 75:
        status = "pleasant"
    else:
        status = "hot"

    return status

def main():
    print()

    

if __name__ == "__main__":
    main()
