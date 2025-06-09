import random

if __name__ != "__main__":
    from autograder_assistant import input

def order_combo_meal(sandwich, side, drink):
    p1 = get_item_price("sandwich", sandwich)
    p2 = get_item_price("side", side)
    p3 = get_item_price("drink", drink)
    total = p1 + p2 + p3
    valid = validate_meal(sandwich, side, drink)
    return total, valid

def get_item_price(item, num):
    price = 0.0
    if item == "sandwich":
        if num == 1:
            price = 1.99
        elif num == 2:
            price = 2.45
        elif num == 3:
            price = 4.44            
    elif item == "side":
        if num == 1:
            price = 1.99
        elif num == 2:
            price = 2.99
    else:
        if num == 1:
            price = 1.00
        elif num == 2:
            price = 1.50
        elif num == 3:
            price = 2.00
        elif num == 4:
            price = 3.99            
    return price
    

def validate_meal(sandwich, side, drink):
    valid = True
    if sandwich < 1 or sandwich > 3:
        valid = False
    if side < 1 or side > 2:
        valid = False
    if drink < 1 or drink > 4:
        valid = False
    return valid


def generate_lock_combination():
    num1 = generate_number()
    num2 = generate_number()
    num3 = generate_number()
    return num1, num2, num3

def generate_number():
    return random.randint(0, 39)

def validate_combination(num1, num2, num3):
    valid = True
    if num1 < 0 or num1 > 39 or num2 < 0 or num2 > 39 or num3 < 0 or num3 > 39:
        valid = False
    if num1 == num2 or num2 == num3:
        valid = False

    return valid


def get_quantities():
    s = int(input("Enter s: "))
    m = int(input("Enter m: "))
    l = int(input("Enter l: "))
    xl = int(input("Enter xl: "))
    xxl = int(input("Enter xxl: "))
    xxxl = int(input("Enter xxxl: "))
    return s, m, l, xl, xxl, xxxl

def get_estimate():
    s, m, l, xl, xxl, xxxl = get_quantities()
    estimate = s*5 + m*7 + l*10 +xl*12 + xxl*13 + xxxl*15
    return estimate



def main():
    #autograde()
    total = get_estimate()
    print("total cost:", total)
    #return total

    num1, num2, num3 = generate_lock_combination()
    result = validate_combination(num1, num2, num3)
    
    sandwich = int(input("Enter sandwich number: (1, 2, 3)"))
    side = int(input("Enter side number: (1, 2)"))    
    drink = int(input("Enter drink number: (1, 2, 3, 4)"))
    price, result = order_combo_meal(sandwich, side, drink)
    print("Combo Meal")
    print("Sandwich: " + str(sandwich))
    print("Side: " + str(side))
    print("Drink: " + str(drink))
    print("Cost: " + str(price))
    if result == True:
        print("Valid Meal")
    else:
        print("Invalid Meal")


if __name__ == "__main__":
    main()
