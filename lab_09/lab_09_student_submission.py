# Name:
# Date:
# Purpose: Lists lab 1

import csc170_lists_data

# 1
l_cities = []

# 2
l_miles = [3.1, 6.2, 13.1, 26.2]

# 3
f_third = l_miles[3]

# 4
l_states = ["KY", "IN", "TN", "WV"]
l_states[0] = "MA"

# 5
s_state = l_states[1]

# 6
l_countries = ["US", "Japan", "Brazil", "Mexico"]
l_countries.append("Canada")

# 7
l_cars = ["Ferrari", "Bug", "Rio", "Corolla", "Maserati"]
l_cars.insert(1, "Sonata")

# 8
l_names = csc170_lists_data.get_q8_list()
del l_names[1]

# 9
l_names2 = csc170_lists_data.get_q8_list()
l_names2.remove("Theodore")

# 10
i_num_names = len(l_names2)

# 11
if "Camry" in l_cars:
    b_camry_present = True
else:
    b_camry_present = False

if "Sonata" in l_cars:
    b_sonata_present = True
else:
    b_sonata_present = False

# 12
if "Suzy" in l_names:
    i_suzy_location = l_names.index("Suzy")
else:
    i_suzy_location = -1
if "Dave" in l_names:
    i_dave_location = l_names.index("Dave")
else:
    i_dave_location = -1

# 13
l_grades = csc170_lists_data.get_q13_list()
for index in range(len(l_grades)):
    l_grades[index] = l_grades[index] + 2
print(l_grades)

# 14
l_grades2 = csc170_lists_data.get_q13_list()
l_grades2.sort()

# 15
l_grades3 = csc170_lists_data.get_q13_list()
l_grades3.sort()
l_grades3.reverse()

# 16
i_biggest = max(l_grades3)

# 17
i_smallest = min(l_grades3)


def main():
    pass

if __name__ == "__main__":
    main()
