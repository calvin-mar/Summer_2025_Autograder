if __name__ != "__main__":
    from autograder_assistant import input

def biggest_number():
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
    counter = 0
    while counter < times_to_double:
        num_to_double = num_to_double * 2
        counter = counter + 1
    return num_to_double

def fib_num(num):
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

def make_bill():
    total = 0.0

    item = input("enter item name or done to quit")
    while item != "done":
        # grab price
        price = 0.0
        while price <= 0.0:
            price = float(input("Enter price: "))

        # grab qty
        qty = 0
        while qty <= 0:
            qty = int(input("Enter qty: "))

        # add to bill
        total = total + price * qty
        
        # grab next item
        item = input("enter item name or done to quit")

    total = total + total * .065
    total = total + total * .2   
    return total



def is_prime(num):
    res = True
    counter = 2
    if num == 1:
        res = False
    elif num == 2:
        res = True
    else:
        while counter < num:
            if num % counter == 0:
                res = False
            counter = counter + 1
    return res

def count_primes(target):
    total = 0
    counter = 1
    while counter <= target:
        if is_prime(counter) == True:
            total = total + 1
        counter = counter + 1
    return total


def main():
    
    print("========= finding biggest number")
    res = biggest_number()
    print(res)
    
    print("========= double number repeatedly")
    num_to_double = int(input("enter number to double: "))
    times_to_double = int(input("enter how many times to double: "))    
    res = repeated_doubler(num_to_double, times_to_double)
    print(res)
    
    print("========= fibonacci numbers")
    fib_number = int(input("Which fib num do you want? "))
    res = fib_num(fib_number)
    print(res)
    
    print("========= restaurant check")
    res = make_bill()
    print(res)
    
    print("========= prime numbers")
    target = int(input("Enter positive number: "))
    while target < 1:
        target = int(input("Enter positive number: "))
        
    res = count_primes(target)
    print(res)
    

if __name__ == "__main__":
    main()
