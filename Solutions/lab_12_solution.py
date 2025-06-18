# Name:
# Date:
# Purpose: Strings lab 1
if __name__ != "__main__":
    from autograder_assistant import input
    
import csc170_strings_data
from csc170_strings_data import *

s_task_1_data = get_q1_string()
s_task_2_data = get_q2_string()
s_task_3_A_data, s_task_3_B_data = get_q3_string()
s_task_4_data = get_q4_string()
s_task_5_data = get_q5_string()
s_task_6_data = get_q6_string()
s_task_7_data = get_q7_string()
s_task_9_data_A, s_task_9_data_B = get_q9_string()
s_task_12_data = get_q12_string()
s_task_13_data = get_q13_string()
s_task_14_data = get_q14_string()
s_task_15_data = get_q15_string()
s_task_16_data = get_q16_string()
s_task_17_A_data, s_task_17_B_data = get_q17_string()
s_task_18_data = get_q18_string()
s_task_19_data = get_q19_string()
s_task_20_data = get_q20_string()
s_task_23_data = get_q23_string()
s_task_24_data = get_q24_string()
s_task_25_A_data, s_task_25_B_data = get_q25_string()
s_task_26_data = get_q26_string()
s_task_27_data = get_q27_string()



# 1
i_task_1 = len(s_task_1_data)

# 2
s_task_2 = s_task_2_data[6]

# 3
if s_task_3_A_data == s_task_3_B_data:
    b_task_3 = True
else:
    b_task_3 = False

# 4
s_task_4 = s_task_4_data.strip()

# 5
if "abc" in s_task_5_data:
    b_task_5 = True
else:
    b_task_5 = False

# 6
if "sally" not in s_task_6_data:
    b_task_6 = True
else:
    b_task_6= False

# 7
l_task_7 = s_task_7_data.split(":")

# 8
i_task_8_start = 5
i_task_8_stop = 10

# 9
s_task_9 = s_task_9_data_A + s_task_9_data_B

# 10
s_task_10 = ""

for index in range(len(l_task_7)-1, -1, -1):
    s_task_10 = s_task_10 + l_task_7[index]

# 11
i_task_11_end = 6

# 12
if "a1b2c3" not in s_task_12_data:
    b_task_12 = True
else:
    b_task_12 = False

# 13
if "ok" in s_task_13_data:
    b_task_13 = True
else:
    b_task_13 = False

# 14
i_task_14 = len(s_task_14_data)

# 15
s_task_15 = s_task_15_data[1]

# 16
if "pop" in s_task_16_data:
    b_task_16 = True
else:
    b_task_16 = False

# 17
if s_task_17_A_data == s_task_17_B_data:
    b_task_17 = True
else:
    b_task_17 = False

# 18
if "xyz" not in s_task_18_data:
    b_task_18 = True
else:
    b_task_18 = False

# 19
s_task_19 = s_task_19_data.strip()

# 20
l_task_20 = s_task_20_data.split(", ")

# 21
i_task_21_start = 4

# 22
s_task_22 = ""
for item in l_task_7:
    s_task_22 = s_task_22 + item

# 23
i_task_23 = len(s_task_23_data)

# 24
s_task_24 = s_task_24_data.strip()

# 25
if s_task_25_A_data == s_task_25_B_data:
    b_task_25 = True
else:
    b_task_25 = False

# 26
s_task_26 = s_task_26_data[3]

# 27
l_task_27 = s_task_27_data.split("ball")


def main():
    pass

if __name__ == "__main__":
    main()
