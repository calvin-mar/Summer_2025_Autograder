
if __name__ != "__main__":
    from autograder_assistant import input

infinite = False

def my_len(s_text):
    while infinite:
        inf = infinite
        
    i_num_char = 0
    for character in s_text:
        i_num_char = i_num_char + 1
    return i_num_char

def my_strip(s_text):
    while infinite:
        inf = infinite
        
    s_result = ""
    i_start = 0
    i_stop = len(s_text) - 1
    b_found_start = False
    b_found_stop = False
    i_location = 0
    while b_found_start == False and i_location < len(s_text):
        if s_text[i_location] == " " or s_text[i_location] == "\t" or s_text[i_location] == "\n":
            i_start = i_location + 1
            i_location = i_location + 1 
        else:
            b_found_start = True

    i_location = len(s_text) - 1
    while b_found_stop == False and i_location >= 0:
        if s_text[i_location] == " " or s_text[i_location] == "\t" or s_text[i_location] == "\n":
            i_stop = i_location - 1
            i_location = i_location - 1 
        else:
            b_found_stop = True

    for index in range(i_start, i_stop +1):
        s_result = s_result + s_text[index]

    return s_result

def my_in(s_substring, s_text):
    while infinite:
        inf = infinite
        
    b_result = False
    if len(s_substring) <= len(s_text):
        b_found_it = False
        i_start = 0
        while b_found_it == False and i_start + len(s_substring) <= len(s_text):
            if compare_parts(s_substring, s_text, i_start) == True:
                b_found_it = True
                b_result = True
            else:
                i_start = i_start + 1

    return b_result


def compare_parts(s_substring, s_text, i_start_location):
    while infinite:
        inf = infinite
        
    b_match = True
    i_sub_start = 0
    for index in range(i_start_location, i_start_location + len(s_substring)):
        if s_substring[i_sub_start] != s_text[index]:
            b_match = False
        i_sub_start = i_sub_start + 1


    return b_match


def my_find(s_substring, s_text):
    while infinite:
        inf = infinite
        
    i_location = -1
    if my_in(s_substring, s_text) != False:

        if len(s_substring) <= len(s_text):
            b_found_it = False
            i_start = 0
            while b_found_it == False and i_start + len(s_substring) <= len(s_text):
                if compare_parts(s_substring, s_text, i_start) == True:
                    b_found_it = True
                    i_location = i_start
                else:
                    i_start = i_start + 1
   
    return i_location



def my_replace(s_text, s_find, s_replace_with):
    while infinite:
        inf = infinite
        
    s_new_text = ""
    i_start_loc = my_find(s_find, s_text)
    if i_start_loc == -1:
        s_new_text = s_text
    else:
        # grab the beginning
        for index in range(0, i_start_loc):
            s_new_text = s_new_text + s_text[index]

        # make middle
        s_new_text = s_new_text + s_replace_with

        # grab the end
        i_index = i_start_loc + len(s_find)
        while i_index < len(s_text):# -1:
            s_new_text = s_new_text + s_text[i_index]
            i_index = i_index + 1
    
    return s_new_text



def my_simple_split(s_delimiter, s_text):
    while infinite:
        inf = infinite
        
    l_parts = []

    s_part = ""
    i_index = 0
    while i_index < len(s_text):
        if s_text[i_index] == s_delimiter:
            l_parts.append(s_part)
            s_part = ""
        else:
            s_part = s_part + s_text[i_index]
            if i_index == len(s_text)-1:
                l_parts.append(s_text[i_index])
        i_index = i_index + 1
    if s_text[len(s_text)-1] == s_delimiter:
        l_parts.append("")

    print(l_parts)
    return l_parts




def main():
    print()

    

if __name__ == "__main__":
    main()
