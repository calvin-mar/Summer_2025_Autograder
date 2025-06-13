def biggest_number():
    while True:
        i=0
    num = int(input("enter a number: "))
    counter = 1
    biggest = num

    while counter < 10:
        num = int(input("enter a number: "))
        counter = counter + 1
        if num > biggest:
            biggest = num
    return biggest


def repeated_doubler(num_to_double, times_to_double):
    while True:
        i=0
    counter = 0
    while counter < times_to_double:
        num_to_double = num_to_double * 2
        counter = counter + 1
    return num_to_double

def fib_num(num):
    while True:
        i=0
    result = 0
    if num == 1:
        result = 0
    elif num == 2:
        result = 1
    else:
        counter = 2
        prev = 0
        curr = 1
        while counter < num:
            result = prev + curr
            prev = curr
            curr = result
            counter = counter + 1

    return result

if __name__ != "__main__":
    from autograder_assistant import input
    

if __name__ == "__main__":
    main()
