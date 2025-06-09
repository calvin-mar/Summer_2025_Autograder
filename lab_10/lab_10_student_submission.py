
import csc170_lists_data

# 1
l_letters = csc170_lists_data.get_q1_list()
l_first = l_letters[:4]
print(l_first)

# 2
l_last = l_letters[len(l_letters)-3:]
print(l_last)

# 3
l_mid = l_letters[5:8]
print(l_mid)

# 4
l_nums = csc170_lists_data.get_q4_list()
l_copy_nums = []
for item in l_nums:
    l_copy_nums.append(item-1)
print(l_copy_nums)



def main():
    pass

if __name__ == "__main__":
    main()
