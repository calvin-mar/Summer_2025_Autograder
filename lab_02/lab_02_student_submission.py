# Name: 
# Purpose: CSC 170, Lab 2, Arithmetic

if __name__ != "__main__":
    from input_override import input,print

f_miles = float(input("Enter the number of miles "))
f_distance_km = (f_miles / 3.1) * 5
print(str(f_miles) + " miles is " + str(f_distance_km) + " km")

f_small_area = 3.14 * 6 ** 2
f_med_area = 3.14 * 8 ** 2
f_large_area = 3.14 * 9 ** 2
f_small_cost = 8 / f_small_area
f_med_cost = 12 / f_med_area
f_large_cost = 16 / f_large_area
