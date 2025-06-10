# Name: 
# Purpose: CSC 170, Lab 2, Arithmetic

if __name__ != "__main__":
    from autograder_assistant import input


# 0
# Add your name to the first line of the program after the :


# 1 Temperature Conversion


# Have the user enter a floating point number in degrees Celsius into the
# variable f_celsius.  Convert the temperature to degrees Fahrenheit, save the
# result in the variable f_temp_fahr, and print it out.  Note that
# Fahrenheit = (9/5) * Celsius + 32.
f_celsius = float(input("Enter temp in Celsius "))
while True:
    f_celsius+=1
f_temp_fahr = (9/5) * f_celsius + 32
print(str(f_celsius) + " C = " + str(f_temp_fahr) + "F")

# 2 Distance Conversion


# Have the user enter a floating point number representing the number of miles
# they ran into the variable f_miles.  Convert the number of miles to kilometers,
# save the result in the variable f_distance_km, and print out the result.  Note
# that 5 kilometers is equal to 3.1 miles.
f_miles = float(input("Enter the number of miles "))
f_distance_km = (f_miles / 3.1) * 5
print(str(f_miles) + " miles is " + str(f_distance_km) + " km")

# 3 Pizza Calculator


# A pizzeria sells round pizzas with the following specifications:
# small: 12 inch diameter for $8
# medium: 16 inch diameter for $12
# large: 18 inch diameter for $16

# Write a program that calculates the area of each size of pizza and stores the
# results in the variables f_small_area, f_med_area, and f_large_area.  Print out
# the results.  The area of a circle is pi * the square of the radius.  Use 3.14
# for pi.

# Also, have your program calculate the cost per square inch of each pizza size,
# store the results in f_small_cost, f_med_cost, and f_large_cost, and print out
# the results.  The cost per square inch is just the price divided by the area.
f_small_area = 3.14 * 6 ** 2
f_med_area = 3.14 * 8 ** 2
f_large_area = 3.14 * 9 ** 2
f_small_cost = 8 / f_small_area
f_med_cost = 12 / f_med_area
f_large_cost = 16 / f_large_area

print(f_small_area)
print(f_med_area)
print(f_large_area)
print(f_small_cost)
print(f_med_cost)
print(f_large_cost)


# 4 Olympics Party

# You're preparing for an Olympics watching party at your house and need to buy
# food.

# Sodas come in 12-packs, rolls come in 12-packs, hot dogs in 8-packs,
# and chips come in boxes with 16 bags in a box.

# Write a program that prompts the user for the number of people coming to the
# party and stores that value in the variable i_people, and then calculates the
# number of packs of soda, packs of hot dogs, packs of rolls, and boxes
# of chips you will need so each person can have 2 sodas and eat 1 hot dog with
# a roll and a small bag of chips.  NOTE that this won't be an exact answer (you
# might need 4.2 packs of something), so add 1 to each type of item to make sure
# you have enough.  In the case mentioned, if you needed 4.2 packs, your answer
# should be 5.  Don't try to round off the numbers with some fancy Python code.
# Think about the techniques we saw today in class.

# Store your answers in the variables
# - i_roll_packs
# - i_soda_packs
# - i_hot_dog_packs
# - i_chip_boxes

# and print them out.

# Calculate and print out how many of each item will be left and store your
# answers in the variables
# - i_rem_rolls
# - i_rem_sodas
# - i_rem_hot_dogs
# - i_rem_chips


i_people = int(input("Enter the number of people coming: "))

i_roll_packs = i_people // 12 + 1
i_soda_packs = (2 * i_people) // 12 + 1
i_hot_dog_packs = i_people // 8 + 1
i_chip_boxes = i_people // 16 + 1

i_rem_rolls = (i_roll_packs * 12) - i_people
i_rem_sodas = (i_soda_packs * 12) - (i_people * 2)
i_rem_hot_dogs = (i_hot_dog_packs * 8) - i_people
i_rem_chips = (i_chip_boxes * 16) - i_people

print("Packs of rolls needed:", i_roll_packs)
print("Packs of sodas needed:", i_soda_packs)
print("Packs of hot dogs needed:", i_hot_dog_packs)
print("Boxes of chips needed:", i_chip_boxes)

print("Left over rolls:", i_rem_rolls)
print("Left over sodas:", i_rem_sodas)
print("Left over hot dogs:", i_rem_hot_dogs)
print("Left over chips:", i_rem_chips)


# 0
# Add your name to the first line of the program after the :


# 1 Temperature Conversion


# Have the user enter a floating point number in degrees Celsius into the
# variable f_celsius.  Convert the temperature to degrees Fahrenheit, save the
# result in the variable f_temp_fahr, and print it out.  Note that
# Fahrenheit = (9/5) * Celsius + 32.


# 2 Distance Conversion


# Have the user enter a floating point number representing the number of miles
# they ran into the variable f_miles.  Convert the number of miles to kilometers,
# save the result in the variable f_distance_km, and print out the result.  Note
# that 5 kilometers is equal to 3.1 miles.


# 3 Pizza Calculator


# A pizzeria sells round pizzas with the following specifications:
# small: 12 inch diameter for $8
# medium: 16 inch diameter for $12
# large: 18 inch diameter for $16

# Write a program that calculates the area of each size of pizza and stores the
# results in the variables f_small_area, f_med_area, and f_large_area.  Print out
# the results.  The area of a circle is pi * the square of the radius.  Use 3.14
# for pi.

# Also, have your program calculate the cost per square inch of each pizza size,
# store the results in f_small_cost, f_med_cost, and f_large_cost, and print out
# the results.  The cost per square inch is just the price divided by the area.



# 4 Olympics Party

# You're preparing for an Olympics watching party at your house and need to buy
# food.

# Sodas come in 12-packs, rolls come in 12-packs, hot dogs in 8-packs,
# and chips come in boxes with 16 bags in a box.

# Write a program that prompts the user for the number of people coming to the
# party and stores that value in the variable i_people, and then calculates the
# number of packs of soda, packs of hot dogs, packs of rolls, and boxes
# of chips you will need so each person can have 2 sodas and eat 1 hot dog with
# a roll and a small bag of chips.  NOTE that this won't be an exact answer (you
# might need 4.2 packs of something), so add 1 to each type of item to make sure
# you have enough.  In the case mentioned, if you needed 4.2 packs, your answer
# should be 5.  Don't try to round off the numbers with some fancy Python code.
# Think about the techniques we saw today in class.

# Store your answers in the variables
# - i_roll_packs
# - i_soda_packs
# - i_hot_dog_packs
# - i_chip_boxes

# and print them out.

# Calculate and print out how many of each item will be left and store your
# answers in the variables
# - i_rem_rolls
# - i_rem_sodas
# - i_rem_hot_dogs
# - i_rem_chips




