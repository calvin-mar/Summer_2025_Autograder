if __name__ != "__main__":
    from autograder_assistant import input


def biggest_smallest_number():
    num = int(input("enter a number: "))
    counter = 1
    biggest = num
    smallest = num

    while counter < 10:
        num = int(input("enter a number: "))
        counter = counter + 1
        if num > biggest:
            biggest = num
        if num < smallest:
            smallest = num
    return biggest, smallest


def repeated_doubler(num_to_double, times_to_double):
    for index in range(times_to_double):
        num_to_double = num_to_double * 2
    return num_to_double

def fib_num(num):
    result = 0
    if num == 1:
        result = 0
    elif num == 2:
        result = 1
    else:
        prev = 0
        curr = 1
        for index in range(num - 2):
            result = prev + curr
            prev = curr
            curr = result

    return result



def leaf_sum(days):
    total = 0
    for index in range(days):
        leaves = int(input("how many leaves today? "))
        total = total + leaves
    return total

def class_leaf_sum(students):
    total = 0
    print("test")
    for index in range(students):
        days = int(input("how many days did this student collect? "))
        leaves = leaf_sum(days)
        total = total + leaves
        print(index)
    return total
        


def main():
    
    print("========= finding biggest number")
    b, s = biggest_smallest_number()
    print(b, s)

    print("========= double number repeatedly")
    num_to_double = int(input("enter number to double: "))
    times_to_double = int(input("enter how many times to double: "))    
    res = repeated_doubler(num_to_double, times_to_double)
    print(res)

    print("========= fibonacci numbers")
    fib_number = int(input("Which fib num do you want? "))
    res = fib_num(fib_number)
    print(res)

    print("========= collecting leaves part 1")
    days = int(input("how many days did this student collect? "))
    res = leaf_sum(days)
    print(res)
    
    print("========= collecting leaves part 2")
    students = int(input("how many students in class? "))
    res = class_leaf_sum(students)
    print(res)



if __name__ == "__main__":
    main()
