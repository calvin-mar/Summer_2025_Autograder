if __name__ != "__main__":
    from input_override import input, print

def biggest_number():
    num = int(input("enter a number: "))
    counter = 1
    biggest = num

    while counter < 5:
        num = int(input("enter a number: "))
        counter = counter + 1
        if num > biggest:
            biggest = num
    return biggest

if __name__ == "__main__":
    main()
