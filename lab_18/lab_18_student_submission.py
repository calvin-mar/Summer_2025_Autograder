
if __name__ != "__main__":
    from autograder_assistant import input


    
def get_data():
    # Get all candy data
    input_file = open("candy_data.txt", "r")
    l_candy_data = input_file.readlines()
    input_file.close()

    # Strip off all new lines
    for index in range(len(l_candy_data)):
        l_candy_data[index] = l_candy_data[index].strip()

    # Make the big 2d list
    l2d_candy = []

    for index in range(len(l_candy_data) // 9):
        l_row = []
        l_row.append(l_candy_data[(index * 9) + 0])
        l_row.append(l_candy_data[(index * 9) + 1])
        l_row.append(l_candy_data[(index * 9) + 2])
        l_row.append(l_candy_data[(index * 9) + 3])
        l_row.append(l_candy_data[(index * 9) + 4])
        l_row.append(l_candy_data[(index * 9) + 5])
        l_row.append(l_candy_data[(index * 9) + 6])
        l_row.append(l_candy_data[(index * 9) + 7])
        l_row.append(l_candy_data[(index * 9) + 8])
        l2d_candy.append(l_row)

    return l2d_candy


def get_avg_sat_fat(l2d_candy):

    i_num_items = 0
    f_total_sat_fat = 0
    for row in range(len(l2d_candy)):
        s_fat = l2d_candy[row][4]
        if s_fat != "n/a":
            i_num_items = i_num_items + 1
            f_sat_fat = float(s_fat.strip("g"))
            f_total_sat_fat = f_total_sat_fat + f_sat_fat
    return f_total_sat_fat / i_num_items


def add_allergy_info(l2d_candy):

    l2d_allergy = []

    # add the two columns
    for index in range(len(l2d_candy)):
        row = l2d_candy[index]
        allergy_row = []
        for item in row:
            allergy_row.append(item)
        #allergy_row.append("")
        #allergy_row.append("")
        l2d_allergy.append(allergy_row)

    # load nuts & chocolate data
    input_file = open("nuts.txt", "r")
    l_nuts = input_file.readlines()
    input_file.close()

    for index in range(len(l_nuts)):
        l_nuts[index] = l_nuts[index].strip()

    input_file = open("chocolate.txt", "r")
    l_chocolate = input_file.readlines()
    input_file.close()

    for index in range(len(l_chocolate)):
        l_chocolate[index] = l_chocolate[index].strip()

    # update new 2d list with nuts & chocolate data
    for row in range(len(l2d_allergy)):
        if l2d_allergy[row][0] in l_nuts:
            l2d_allergy[row][9] = True
        else:
            l2d_allergy[row][9] = False
            
        if l2d_allergy[row][0] in l_chocolate:
            l2d_allergy[row][10] = True
        else:
            l2d_allergy[row][10] = False

    return l2d_allergy

def write_safe_candies(l2d_allergy):

    output_file = open("safe.csv", "w")
    for row in range(len(l2d_allergy)):
        if l2d_allergy[row][9] == False and l2d_allergy[row][10] == False:
            sodium = float(l2d_allergy[row][7].strip("mg"))
            if sodium < 50:
                output_file.write(l2d_allergy[row][0] + "," + l2d_allergy[row][7] + "," + l2d_allergy[row][2] + "\n")
    output_file.close()


def main():
    l2d_data = get_data()
    print(get_avg_sat_fat(l2d_data))
    l2d_alg = add_allergy_info(l2d_data)
    print(l2d_alg)
    write_safe_candies(l2d_alg)
    
    print()

if __name__ == "__main__":
    main()
