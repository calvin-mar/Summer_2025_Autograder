
def double_a_number(x):
    return 2 * x


def biggest_number(a, b, c):
    biggest = a
    if b > biggest:
        biggest = b
    if c > biggest:
        biggest = c
    return biggest    

def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

def rectangle_area(l, w):
    return l * w

def km_to_miles(km):
    return km * 3.1 /5

def is_leap_year(y):
    if y % 4 != 0:
        return False
    else:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
    return True

def main():
    print()

##    Test cases

##    # list comprehension
##    input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
##    list_using_comp = [var for var in input_list if var % 2 == 0]
##    print("Output List using list comprehensions:", list_using_comp)
##
##    # another list comprehension - not caught yet
##    list_using_comp = [var**2 for var in range(1, 10)]
##
##    # dictionary comprehension
##    dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0}
##
##    # another dictionary comprehension
##    input_list = [1,2,3,4,5,6,7]
##    dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0}
##    print("Output Dictionary using dictionary comprehensions:",dict_using_comp)
##
##    # set comprehension
##    input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
##    set_using_comp = {var for var in input_list if var % 2 == 0}
##    print("Output Set using set comprehensions:", set_using_comp)
##
##    # generator comprehension
##    input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
##    output_gen = (var for var in input_list if var % 2 == 0)
##    print("Output values using generator comprehensions:", end = ' ')


##    for i in range(4):
##        continue

##    for i in range(4):
##        break

### using with statement
##    with open('sillytest.txt', 'w') as file:
##        file.write('hello world !')

##    with open ('sillytest.txt', 'w') as file:
##        file.write('hello world !')


##    quit()

##    exit()

##    _ = 5

##    a = "f".join("f")

##    print("join(")

##    #join()
    
##    print("return.")

##    print("return")

##    print(" _ =")

##    _ = 5

    print()

if __name__ == "__main__":
    main()

