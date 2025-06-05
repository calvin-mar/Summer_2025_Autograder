def compare_lists_2d(l2d_list1, l2d_list2):
    b_same = True
    # compare shape of the lists
    # num rows
    if len(l2d_list1) == len(l2d_list2):

        # num columns in each row
        for index in range(len(l2d_list1)):
            if len(l2d_list1[index]) != len(l2d_list2[index]):
                b_same = False
                #print("num cols not same")


        if b_same == True:
            # lists are same shape - compare them item by item now
            for row in range(len(l2d_list1)):
                for col in range(len(l2d_list1[row])):
                    if l2d_list1[row][col] != l2d_list2[row][col]:
                        b_same = False
                        #print("value not same")
    else:
        b_same = False
        #print("num rows not same")

    return b_same
    
def main():
    print()

    

if __name__ == "__main__":
    main()
