if __name__ != "__main__":
    from input_override import input, print
    
def repeated_doubler(num_to_double, times_to_double):
    counter = 0
    while counter < times_to_double:
        num_to_double = num_to_double * 2
        counter = counter + 1
    return num_to_double

if __name__ == "__main__":
    main()
